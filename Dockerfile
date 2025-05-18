# Use an official Ubuntu base image
FROM ubuntu:latest

# Set the working directory inside the container
WORKDIR /app

# Copy all files from current directory on host to /app in the container
COPY . /app

# Install Python
RUN apt-get update && apt-get install -y python3

# Set the command to run the Python script
CMD ["python3", "app.py"]

