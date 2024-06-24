# Use the official Rasa image
FROM rasa/rasa:latest-full

# Switch to root user to install packages
USER root

# Install supervisord
RUN apt-get update && apt-get install -y supervisor

# Set environment variables
ENV RASA_ACTION_PORT=5055

# Set working directory
WORKDIR /app

# Copy all project files into the container
COPY . /app




# Install Python dependencies
RUN pip install -r requirements.txt

# Expose the ports for Rasa and Rasa actions
EXPOSE 5005 5055

# Copy supervisord configuration
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Switch back to a non-root user
USER 1001

# Ensure the path is set correctly
ENV PATH="/usr/bin:/usr/local/bin:/app/.local/bin:${PATH}"

# Run supervisord
CMD [ "run", "--enable-api", "--cors", "*"] && CMD ["run", "actions"]