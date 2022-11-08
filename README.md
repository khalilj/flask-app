# flask-app
This is Flask app main repository

Flask app is an awsome app

# Running The Server
```
python flask-app.py
```

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 821594384510.dkr.ecr.us-east-1.amazonaws.com
docker tag flask-app:1.0.0 821594384510.dkr.ecr.us-east-1.amazonaws.com/flask-app:1.0.0
docker push 821594384510.dkr.ecr.us-east-1.amazonaws.com/flask-app:1.0.0
