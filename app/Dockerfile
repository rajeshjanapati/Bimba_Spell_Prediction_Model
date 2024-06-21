FROM rasa/rasa:latest-full

# Install supervisord
RUN apt-get update && apt-get install -y supervisor

# Set environment variables
ENV RASA_ACTION_PORT=5055

# Copy Rasa files
COPY . /app

# Set working directory
WORKDIR /app

# Install any additional dependencies
RUN pip install -r requirements.txt

# Copy supervisord configuration
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose the ports for Rasa and Rasa actions
EXPOSE 5005 5055

# Run supervisord
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
