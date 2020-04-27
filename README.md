# Strike Zone application and backend
-------------------------------------

## Folders
- front_end: sources for android application.
- backend: sources for backend - dockers and image processing code

## I - FRONTEND
## 1. Setup
- Installer les dépendances js
```shell
cd front_end/
npm i
sudo npm install -g webpack
sudo npm install -g vue
sudo npm install -g cordova
sudo apt install default-jdk openjdk-8-jdk openjdk-8-jre gradle
```
- Installer la bonne version du sdk android (celle correspondant au téléphone): https://developer.android.com/studio/index.html#download
Installer Android studio et passer par la GUI (tools/sdk) ou installer la cli -> Command line tools only (il faut acceter les conditions d'utilisation dans tous les cas)

- Compiler les applications:
dans le dossier front_end

```shell
npm run dev
```

## 2. Deploiement sur android
Ajouter les lignes suivantes, complétées, dans le .bashrc
export ANDROID_SDK_ROOT=<path_to_android_Sdk_folder>
export PATH=$ANDROID_SDK_ROOT/platform-tools:<android-studio_folder>/bin:$PATH>

```shell
cd cordova/
cordova platform add android
cd ../
npm run build:android
cd cordova/
```
Brancher le telephone au pc puis
```shell
cordova run android
```
--> l'application doir se lander sur le téléphone.

Si l'application ne demande pas l'accès à la caméra, aller dans les paramètres système et ajouter la permission caméra pour l'application.


-------------------------------------
-------------------------------------
## II - BACKEND

## 1. Libsocket:
C/C++ librarie utilisée pour du networking. Il faut l'installer de puis son dépot github:
```shell
cd backend
git clone https://github.com/dermesser/libsocket.git
cd libsocket
mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
make
sudo make install
cd ../..
```

## 2. Docker & docker-compose:
Checker si docker-compose est installé:
```shell
which docker && which docker-compose
```

Si celà ne renvoie pas 2 lignes comme suivant,
```shell
/usr/bin/docker
/usr/bin/docker-compose
```
installer les deux avec la procédure de la doc officielle:
https://docs.docker.com/compose/install

## 3. Create_AP (Point d'accès wifi):

Cette dépendance est utilisée pour créer un point d'accès wifi sur la machine locale qui fera office de backend.
Si vous n'avez pas create_ap d'installé, suivre la procédure suivante.
Installer les dépendances.
```shell
sudo apt-get install util-linux iw iptables iproute2 dnsmasq procps hostapd haveged
```
Installer Create_AP depuis le depot github:
```shell
git clone https://github.com/oblique/create_ap
cd create_ap
sudo make install
cd ..
rm -rf create_ap #if you want to remove the sources
```

Activer the service :
```shell
sudo systemctl start create_ap
sudo systemctl enable create_ap
```

## 4. OPENVINO Pipeline
Maintenant, c'est du lourd...

**Warning** !!
Attention, si vous avez déjà installé le projet ROS pour Numii, il n'est pas nécessaire de refaire toute la procédure d'installation d'OpenVINO et de la pipeline de détection du squelette RGB !! Il suffit de faire un lien dynamic et de passer ensuite au **5.**:

```shell
ln -s <ros_project_folder>/src/prog_kinect/src/human_pose_estimation backend/src/image_processing/rgb_skeleton/human_pose_estimation
```


- **Install d'OpenVINO pour la détection du squelette en RGB:**

Télécharger le toolkit Intel® Distribution of OpenVINO™ depuis 
[Intel® Distribution of OpenVINO™ toolkit for Linux*](https://software.intel.com/en-us/openvino-toolkit/choose-download?elq_cid=5588076&erpm_id=8590667). 
Choisir  Intel® Distribution of OpenVINO™ toolkit for Linux depuis le menu déroulant.
prendre la version `2019 R2.0` pour linux.
Décompresser l'archive téléchargée:
```shell
tar -xvzf l_openvino_toolkit_p_<version>.tgz
cd l_openvino_toolkit_p_<version>
```
Lancer le script d'install avec la GUI (pratique quand on a des yeux ou qu'on est manchot du terminal).
```shell
sudo ./install_GUI.sh
```
Après l'installation, openVINO doit être dans: `/opt/intel/openvino`.
Installer en suivant toutes les dépendances:
```shell
cd /opt/intel/openvino/install_dependencies
sudo -E ./install_openvino_dependencies.sh
```

Finir par rajouter la ligne de chargement des variables d'environnement dans le .bashrc:
```shell 
echo "source /opt/intel/openvino/bin/setupvars.sh >> /dev/null" >> ~/.bashrc
```

- Activer le support GPU (seulement pour les GPU Intel® (ex: NUC))
```shell 
cd /opt/intel/openvino/install_dependencies/
sudo -E su
./install_NEO_OCL_driver.sh
```
Rajouter l'utilisateur courant au group video si ce n'est pas déjà fait:
```shell
sudo usermod -a -G video $USER
```
- Récupérer le code de l'inférence:
```shell
cd ~
git clone ssh://git.aiotools.ovh/numii/human_pose_estimation.git
```
- Génération de la base de donnée squelette 2D <-> squelette 3D

Récupérer la DB des correspondances 2D/3D en téléchargeant le fichier `3D_library.mat` depuis le [Google Drive](https://drive.google.com/file/d/0BxZCS0CAHYZpRjA2S1FsWDNhcEU/view?usp=sharing) et 
la mettre dans le dossier `human_pose_estimation` et executer le script de sous-échantillonage.
```shell
mv ~/Downloads/3D_library.mat ~/human_pose_estimation/model/
cd human_pose_estimation/model
python resize_dataset.py
```

Pour voir le détection tourner, aller dans le dossier `human_pose_estimation/examples` et lancer le notebook jupyter:
```shell
cd ~/human_pose_estimation/examples/
jupyter notebook
```

Maintenant que `human_pose_estimation` est installée, créer un lien dynamique vers le projet strike_zone:
```shell
ln -s ~/human_pose_estimation ~/strike/backend/src/image_processing/rgb_skeleton/human_pose_estimation
```

## 5. Compiler le server TCP pour la détection RGB
La pipeline de l'application est la suivante:
Frontend (image jpg) --> Streaming server (in docker) --> TCP skeleton server (detection du skelette) --> Streaming server (détection in/out strike zone) --> Frontend (label).

(Joli dessin à venir)

Nous allons donc créer le serveur TCP:

Installer Eigen3:
`sudo apt-get install libeigen3-dev`

Compiler le server:
```shell
cd strike/backend/src/image_processing/rgb_skeleton
mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
make
```

## 6. Lancer le backend
Lancer le server RGBSkeleton en premier:
```shell
cd ~/strike/backend/src/image_processing/rgb_skeleton
./build/RGBSkeletonServer
```

Ouvrir un nouveau terminal (ou un nouvel onglet de terminal) et lancer les dockers du backend:
```shell
cd ~/strike/backend
docker-compose up # Add --build if it's the first launch time
```

## 7. Configurer le hotspot wifi pour développer (OPTIONNEL)
Choisir l'interface wifi qui servira de hotspot (ip a pour afficher les interfaces wifi et ethernet disponibles) et éditer la config create_ap en conséquence:

* Il est possible d'utiliser un dongle wifi pour rajouter une interface wifi (d'autant plus que celles-ci supportent toujours create_ap contrairement à certaines interfaces constructeurs).

Editer les lignes comme ceci:
```shell
sudo nano /etc/create_ap.conf
    "GATEWAY=10.0.0.1" => "GATEWAY=192.168.111.1"
    "SHARE_METHOD=nat" => "SHARE_METHOD=none"
    "INTERNET_IFACE=wlan0" => "INTERNET_IFACE="
    "WIFI_IFACE=wlan0" => "WIFI_IFACE=<INTERFACE_WIFI>"
    "SSID=MyAccessPoint" => "SSID=<WhatEverSSIDNameYouWant"
    "PASSPHRASE=12345678" => "PASSPHRASE=<PASSWORD>"
```

Exemple, si mon interface wifi est wlp58b0x:
```shell
sudo nano /etc/create_ap.conf
    "GATEWAY=10.0.0.1" => "GATEWAY=192.168.111.1"
    "SHARE_METHOD=nat" => "SHARE_METHOD=none"
    "INTERNET_IFACE=wlan0" => "INTERNET_IFACE="
    "WIFI_IFACE=wlan0" => "WIFI_IFACE=wlp58b0x"
    "SSID=MyAccessPoint" => "SSID=AwesomeWifiAP"
    "PASSPHRASE=12345678" => "PASSPHRASE=AwesomeMot2Pass"
```

Il faudra ensuite s'assurer que l'interface wifi soit bien mappé sur l'adresse IP statique désirée au lancement pour éviter les conflits avec le network manager linux:

Rajouter les lignes de mapping au fichier `/etc/network/interface`:

```shell
sudo nano /etc/network/interfaces # Pour editer le fichier

...
auto <wifi_interface>
iface <wifi_interface> inet static
	adresse 192.168.111.1
	netmask 255.255.255.0
	gateway 192.168.111.1
```

Ce qui donne pour l'exemple précédent:
```shell
auto wlp58b0x
iface wlp58b0x inet static
	adresse 192.168.111.1
	netmask 255.255.255.0
	gateway 192.168.111.1
```

--> Redémarrer le PC.

--> Vérifier que l'interface réseau est bien `UP` et porte l'adresse IP `192.168.111.1`
(`ip a`)