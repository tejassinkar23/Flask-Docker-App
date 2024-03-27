# Use the official Python image as a base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the content of the local myapp directory to the working directory
COPY . /app

# Install any dependencies your Python application requires
RUN pip install flask

# Expose port 5000
EXPOSE 5000

# Command to run your Python application
CMD ["python", "app.py"]
