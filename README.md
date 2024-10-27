# SpeedOfLight
A jupyter notebook I developed to calculate the speed of light based on ping times to different servers around the globe. The PHYS391 lab only requried a simple calculation of speed of light, but I used a weighted least squares method to get both speed of light, and time per server hop. Furthermore, because I used weighted least squares I was able to properly propagate errors. Using standard least squares doesn't give you a covaraiance matrix for heteroskedastic data. 

I also decided to automate the processes of pinging, and then calculating the intermediate paths from the traceroutes. So thats why there is a script.sh and a dataCleaning.py. It was definitely one of those times where it takes you longer to automate than it does to just do it by hand...
