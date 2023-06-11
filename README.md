# Open Restaurant Backend Server
Repo for Women Who Code FullStack WebDev Project

Skeleton setup here: [docs/Skeleton_Setup.md](docs/Skeleton_Setup.md)


## Development Steps

Using the make commands, you will run:

```bash
make init
make migrate
make seed-data
```

This will give you a migrated database with some seed data in it. 

Verify the server is up by going to: http://localhost:8000/health

If you got to: http://localhost:8000/admin
you can log in by making a superuser with 

```bash
make create-superuser
```

If you want to delete everything and start over use `make nuke`

