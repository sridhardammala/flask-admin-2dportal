# docker build --no-cache --platform linux/amd64 -t europe-west2-docker.pkg.dev/point-cloud-mt/point-cloud-mt-utilities/pcd-utilities:latest .
# docker tag utilities:latest europe-west2-docker.pkg.dev/point-cloud-mt/point-cloud-mt-utilities/pcd-utilities:latest
docker build  -t 
gcloud auth configure-docker europe-west4-docker.pkg.dev
gcloud auth print-access-token | sudo docker login -u oauth2accesstoken --password-stdin https://europe-west2-docker.pkg.dev
docker build -t europe-west2-docker.pkg.dev/point-cloud-mt/github-actions/flaskapi:latest .

docker push europe-west2-docker.pkg.dev/point-cloud-mt/github-actions/flaskapi:latest
