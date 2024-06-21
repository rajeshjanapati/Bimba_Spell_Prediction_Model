# Use the official Rasa image
FROM rasa/rasa:latest-full

# Set environment variables
ENV RASA_ACTION_PORT=5055

# Set working directory
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install supervisord with elevated permissions
USER root
RUN apt-get update && apt-get install -y supervisor

# Switch back to non-root user
USER 1001

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose the ports for Rasa and Rasa actions
EXPOSE 5005 5055

# Copy supervisord configuration
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Run supervisord
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
