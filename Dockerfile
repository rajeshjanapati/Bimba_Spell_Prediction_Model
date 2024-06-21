FROM rasa/rasa-sdk:latest

# Set environment variables
ENV RASA_ACTION_PORT=5055

# Copy actions
COPY actions /app/actions

# Set working directory
WORKDIR /app

# Expose the port
EXPOSE 5055

# Run action server
CMD ["start", "--actions", "actions"]
