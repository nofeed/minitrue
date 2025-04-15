<p align="center">
  <img src="assets/header.png">
</p>

> Configuration as code is the formal migration of config between environments, backed by a version control system.

## What is minitrue?

minitrue is a command line application that helps you manage your configuration. It stores your configuration variables
in your Git repository and encrypts them using GPG.
minitrue is [OpenSource](LICENSE).

## Getting started

```
minitrue init
```
Initializes the current directory as a project configured with minitrue


```
minitrue addkey
```
Adds GPG key from your GPG keychain


```
minitrue set VARIABLE value
```
Sets the VARIABLE to value and encrypts the configuration


```
minitrue addconfig SOURCE DESTINATION
```
Adds a configuration file to your project at SOURCE, to be rendered into DESTINATION


```
minitrue unset
```

