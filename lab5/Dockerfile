FROM ubuntu:latest

# Create a new user and group
RUN groupadd vendors && useradd -m -g vendors cisco

# Set environment variables
ENV username=student 
ENV password=Meilab123 

# Copy script.py into container
COPY script.py /usr/local/bin/script.py

# Make script executable
RUN chmod +x /usr/local/bin/script.py

# Set default command
CMD ["/usr/local/bin/script.py"]
