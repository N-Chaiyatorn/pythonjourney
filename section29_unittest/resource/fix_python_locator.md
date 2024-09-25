# Python locator problem.
This problem is caused by when vs code has been updated to lastest version, sometimes the old python locator can't find your python file which cause extention can't find your project file 
## Solution.
This can fix by insert new data to `setting.json`:
```
<!-- In settion.json -->
{
    ...Same configuration as before,
    "python.locator": "js" 
}
```