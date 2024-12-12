# npm

## package-lock.json

package-lock.json is created based on the rules described in package.json after the "npm install" command. The repositories from which the list of packages in package-lock.json is formed are taken from the npm settings (the "npm config list" command)

## Commands

```bash
npm config set registry 'http://rep.ditsi.ru/artifactory/api/npm/npm'
npm install -g @angular/cli@8.3.6
npm install

# Dockerfile
COPY package.json package-lock.json /tmp/
RUN mv /tmp/node_modules /inventory-front/
RUN cd /inventory-front && ng build --prod

npm i --package-lock-only
```