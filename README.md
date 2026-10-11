# Restconf Automation Script for CCNP
## Description  
This is results of an assignment about making and testing Restconf scripts using Python. It's written and tested by Alihan and Errol in the University West lab Cisco room [D116] alongside with some work at home.

## Features  
- **Grupp** - 13
- **Course** - CCNA [ARS110]
- **Contributers** - Alihan [alsh0015] / Errol [ermu0001]
- **University** - Högskolan Väst

## Lab Enviorment
- 3x Cisco Routers
- Cisco Switch
- Computer
- Applications: Postman, Python IDLE/VSCodium, PuTTY, CMD, Notepad


## Objectives
- Setup Management, restconf and minimal config on each cisco device.
- Write a RESTCONF Python script for an ancient CCNA2 Skills Exam.
- Write a Correction Python Script named after Robert.
- Write conclusions.
- Present it to the rest of the class.

```
|⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|
|⠀⠀⠀⢰⣦⠀⠀⢾⡇⠀⢠⣶⠀⠀⠀⠀⠀⠀⣶⡄⠀⢸⡟⠀⠀⣴⡄⠀⠀⠀|  _____   ______   _____  _______  _____  ____   _   _  ______  |⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|
|⣶⡆⠀⢸⣿⠀⠀⣻⡇⠀⢸⣿⠀⠀⣴⡆⠀⠀⣿⡇⠀⢸⡟⠀⠀⣿⡇⠀⢰⣶| |  __ \ |  ____| / ____||__   __|/ ____|/ __ \ | \ | ||  ____| |⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|
|⠛⠁⠀⠈⠛⠀⠀⣽⡇⠀⠈⠛⠀⠀⠘⠃⠀⠀⠛⠃⠀⢸⣯⠀⠀⠛⠃⠀⠈⠛| | |__) || |__   | (___     | |  | |    | |  | ||  \| || |__    |⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|
|⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀| |  _  / |  __|   \___ \    | |  | |    | |  | || . ` ||  __|   |⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|
|⠀⠀⠀⣠⣶⣶⣶⠀⢰⣶⠀⢀⣴⣶⣶⠀⠀⣤⣶⣶⡆⠀⣀⣶⣶⣦⣄⠀⠀⠀| | | \ \ | |____  ____) |   | |  | |____| |__| || |\  || |      |⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|
|⠀⠀⢠⣿⡃⠀⠀⠀⢸⣿⠀⠘⠿⣶⣤⠀⢸⣿⠁⠀⠀⠠⣿⡃⠀⢘⣿⡆⠀⠀| |_|  \_\|______||_____/    |_|   \_____|\____/ |_| \_||_|      |⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀| 
|⠀⠀⠀⠻⢷⣦⣶⠀⢸⣿⠀⢠⣤⣴⡿⠁⠈⠻⣷⣴⡆⠀⠻⢷⣶⣾⠟⠀⠠⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|
```

## Results and Verification

**Subtask 1 - Setup management and restconf:** 

**Subtask 2 - Write and run the script:**

**Subtask 3 - Write and verify the script:**

## Conclusion

