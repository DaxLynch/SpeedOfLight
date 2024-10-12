#!/bin/bash
tracepath -n berkeley.edu > berkeley.edu.trc   &
tracepath -n cam.ac.uk > cam.ac.uk.trc &
tracepath -n cern.ch > cern.ch.trc &
tracepath -n esunbank.com > esunbank.com.trc &
tracepath -n sun.ac.za > sun.ac.za.trc &
tracepath -n sydney.edu > sydney.edu.au.trc &
tracepath -n uba.ar.trc > uba.ar.trc &
tracepath -n ufl.edu > ufl.edu.trc &
tracepath -n www.ecobank.com > www.ecobank.com.trc &

ping -c 30 berkeley.edu > berkeley.edu.ping   &
ping -c 10 cam.ac.uk > cam.ac.uk.ping &
ping -c 10 cern.ch > cern.ch.ping &
ping -c 10 esunbank.com > esunbank.com.ping &
ping -c 10 sun.ac.za > sun.ac.za.ping &
ping -c 10 sydney.edu > ydney.edu.au.ping &
ping -c 10 uba.ar > uba.ar.ping &
ping -c 10 ufl.edu > ufl.edu.ping &
ping -c 10 www.ecobank.com > www.ecobank.com.ping &

