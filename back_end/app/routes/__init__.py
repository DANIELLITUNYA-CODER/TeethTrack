from .auth import auth
from .patient_route import patient_bp
from .dentist_route import dentist_bp
from .billing_route import billing_bp
from .search_route import search_bp
# from .dashboard_route import dashboard_bp

__all__ = ['auth', 'patient_bp', 'dentist_bp', 'billing_bp', 'search_bp']