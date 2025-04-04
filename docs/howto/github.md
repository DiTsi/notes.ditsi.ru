# GitHub

## GitHub Actions

Code to provide Docker Hub CI process:

```YAML
name: CI

on:
  push:
    branches: 
      - 'master'
    tags: 
      - 'v*'
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Log in to Docker Hub
        uses: docker/login-action@v1
        with:
          username: ${{ secrets.DOCKER_LOGIN }}
          password: ${{ secrets.DOCKER_PASSWORD }}
      - name: Build and push / latest
        uses: docker/build-push-action@v2
        with:
          context: .
          push: true
          tags: ${{ secrets.DOCKER_LOGIN }}/tinkoff_investing_notifier:latest
      - name: Set outputs
        id: vars
        run: echo "::set-output name=sha_short::$(git rev-parse --short HEAD)"
      - name: Build and push / SHA
        uses: docker/build-push-action@v2
        with:
          context: .
          push: true
          tags: ${{ secrets.DOCKER_LOGIN }}/tinkoff_investing_notifier:${{ steps.vars.outputs.sha_short }}
      - name: Extract tag name
        if: startsWith(github.ref, 'refs/tags/v')
        uses: mad9000/actions-find-and-replace-string@2
        id: tag
        with:
          source: ${{ github.ref }} # this translates to ref/heads/main on the main branch, but can be any arbitrary string 
          find: 'refs/tags/'        # we want to remove ref/heads/ from source 
          replace: ''  
      - name: Build and push / tag
        if: startsWith(github.ref, 'refs/tags/v')
        uses: docker/build-push-action@v2
        with:
          context: .
          push: true
          tags: ${{ secrets.DOCKER_LOGIN }}/tinkoff_investing_notifier:${{ steps.tag.outputs.value }}
```
