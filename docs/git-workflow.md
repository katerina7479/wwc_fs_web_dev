## Working with Git


### Typical Git workflow
```
git checkout -b <yourname>/[<ticket#>]_<yourbranch>
```

As you make changes, periodically save your work by running:

```
git add .
git commit -m "Commit message"
git push
```

When you want a PR branch, you can do that on Github. 
You should merge or rebase over main. 

```
git checkout main
git pull
git checkout <branch>
git merge main
...<fix conflicts>
git push
```

Once your changes are merged, you can delete your branch remotely and locally
