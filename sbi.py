git add 1
git status – to check the file status
git commit -m “commit message” (files available in local repository)
git log – it shows commit history
git log --oneline – shows commit history in single line.
1 FROM
Purpose: Specifies the base image for the container.
Syntax:
FROM <image>:<tag>
Example:
FROM node:18
This sets the base image as Node.js version 18.
2  MAINTAINER (Deprecated)
Purpose: Used to specify the author/maintainer of the image (deprecated in favor of LABEL).
Syntax:
MAINTAINER Name <email@example.com>
Example:

MAINTAINER John Doe <john@example.com>
Instead, use LABEL:
LABEL maintainer="John Doe <john@example.com>"
