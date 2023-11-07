# hackathon4

## frontend
### global dependencies
```
npm i -g @capacitor/cli
``` 
(soon maybe dev dependency)

```
npm i -g @ionic/cli
```

### build
#### install dependencies
```
cd ./frontend
yarn install
```
#### build vite
**YOU ALSO NEED DO THIS BEFORE BULD MOBILE APP**
```
yarn build
```
#### build android app
```
yarn install-app-build:android
```
if android studio installed in default path:
```
yarn build:android
```
else:

open folder `android` in Android studio -> go to build -> Generate Signed Bundle/APK
#### build ios app
***soon***

### dev run
```
cd ./frontend
yarn dev
```



