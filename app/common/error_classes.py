class RestrictionError(Exception):
    """Raised when attempting to access plain password"""

    def __init__(self, message="Access to plain password is restricted"):
        self.message = message
        super().__init__(self.message)
