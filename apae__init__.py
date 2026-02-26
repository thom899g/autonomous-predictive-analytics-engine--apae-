"""
Autonomous Predictive Analytics Engine (APAE)
Mission-critical system for autonomous market trend analysis and predictive trading strategies.

Version: 1.0.0
Architect: Evolution Ecosystem Autonomous Architect
Mission: APAE Core Framework
"""

__version__ = "1.0.0"
__author__ = "Evolution Ecosystem Autonomous Architect"
__license__ = "Proprietary"

from .config import APAEConfig
from .data_ingestor import DataIngestor
from .feature_engineer import FeatureEngineer
from .predictive_model import PredictiveModel
from .strategy_engine import StrategyEngine
from .firebase_client import FirebaseClient
from .main import APAEOrchestrator

__all__ = [
    "APAEConfig",
    "DataIngestor",
    "FeatureEngineer",
    "PredictiveModel",
    "StrategyEngine",
    "FirebaseClient",
    "APAEOrchestrator"
]