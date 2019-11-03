#!/bin/bash

echo "Welcome to accident API, by AyoubGL"
echo "############    ############   ###########"
echo "#          #    #          #        #"
echo "#          #    #          #        #"
echo "#          #    #          #        #"
echo "#-ACCIDENT-#    ####-2018-##        #"
echo "#          #    #                   #"
echo "#          #    #                   #"
echo "#          #    #                   #"
echo "#          #    #              ###########"

echo "Create a Python virtual envirenment"
python venv -m ./api_venv
echo "Activate venv"
source api_venv/bin/activate
echo "Install the requirment"
pip install --upgrade pip | pip install -r requirement.txt

echo "Move to api directory"
cd happi_3
echo "Start django api"
python manage.py runserver




