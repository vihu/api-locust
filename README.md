## API Load testing using locust

## Requirements
- docker
- docker-compose

## Run
- Edit "target" in scripts/locust.config.json
- ./run.sh
- Go to localhost:8089
- Enter total users to mock (say 1000)
- Enter users to hatch/s (say 25)
- Don't go too crazy with the total users and hatch rate just yet. It crashes Ranch cuz of file descriptors _shrug_
