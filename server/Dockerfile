FROM python:3.12.0-slim-bookworm

# Set environment variables
ENV PYTHONBUFFERED 1
ENV PYTHONWRITEBYTECODE 1
ENV APP=/app

# Change the working directory
WORKDIR $APP

# Install the requirements
COPY requirements.txt $APP
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . $APP

# Expose the port the application will run on
EXPOSE 8000

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Define the entrypoint script
ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]

# Set the default command to run Gunicorn
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangoproj.wsgi"]