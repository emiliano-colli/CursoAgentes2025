import yfinance as yf
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

# Definimos el esquema de entrada para que el Agente sepa qué enviar
class StockToolInput(BaseModel):
    ticker: str = Field(..., description="El símbolo del ticket de la acción (ej. AAPL, TSLA, MSFT).")

class FinanceTool(BaseTool):
    name: str = "Yahoo Finance Stock Tool"
    description: str = "Útil para obtener precios actuales, noticias y datos financieros de una acción específica usando su ticker."
    args_schema: Type[BaseModel] = StockToolInput

    def _run(self, ticker: str) -> str:
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            
            # Extraemos datos clave
            current_price = info.get('regularMarketPrice') or info.get('currentPrice')
            currency = info.get('currency', 'USD')
            summary = info.get('longBusinessSummary', 'No hay resumen disponible.')
            
            return f"""
            Datos para {ticker}:
            - Precio Actual: {current_price} {currency}
            - Recomendación de Analistas: {info.get('recommendationKey')}
            - Resumen: {summary[:200]}...
            """
        except Exception as e:
            return f"Error al obtener datos para {ticker}: {e}"