"""
Run the Flask development server.
"""

from app import create_app

# Create the app instance using the factory
app = create_app()

if __name__ == "__main__":
    # Run the app with the debug mode specified in config
    app.run()
