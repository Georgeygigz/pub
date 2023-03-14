
echo "<<<<<<< Testing External API calls >>>>>>>>>>"
curl https://a76a-102-219-208-46.ngrok.io

echo "<<<<<<< Install Openssl >>>>>>>>>>"
yum install -y openssl


echo "<<<<<<< Run application >>>>>>>>>>"
python run.py
