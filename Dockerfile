FROM python:3-alpine
LABEL authors="george"
WORKDIR /app
#COPY app.py .
#RUN pip install requests
#CMD ["python3", "app.py"]
#ENTRYPOINT ["top", "-b"]
# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY flask-api.py .

# Expose the port that the Flask app runs on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "flask-api.py"]