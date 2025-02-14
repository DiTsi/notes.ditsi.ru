# gitlab

## Commands

```bash
# show logs for nginx
gitlab-ctl tail nginx

# pushing images to registry
docker push gitlab.domain.com:4567/root/hello_docker/hello_docker:latest
```

## change user password

```bash
# execute line-by-line
gitlab-rails console
  user = User.find_by(email: 'tsibous14@gmail.com')
  user.password = 'new_password'
  user.password_confirmation = 'new_password'
  user.save!
```

## gitlab-runner

```bash
gitlab-runner register -n --url <url> --registration-token <token> --executor docker --description <desc> --docker-image "docker:stable" --docker-privileged
```

## Issues

<p class="callout warning">denied: requested access to the resource is denied</p>

<p class="callout success">The project should be created</p>

## Links

[TLS connection between gitlab-runner и Docker Swarm](https://habr.com/ru/post/344324/)​