# deadwood-mebot
Before deployment, you should configure sudoers like
```commandline
$ visudo -f /etc/sudoers.d/deploy-user-deadwood-mebot

deploy-user ALL=(root) NOPASSWD: /bin/systemctl start deadwood-mebot.service, \
/bin/systemctl stop deadwood-mebot.service, /bin/systemctl restart deadwood-mebot.service, \
/bin/systemctl reload deadwood-mebot.service, /bin/systemctl status deadwood-mebot.service, \
/bin/systemctl disable deadwood-mebot.service, /bin/systemctl enable deadwood-mebot.service, \
/bin/systemctl daemon-reload, /bin/ln -s /path/to/deadwood-mebot.service /etc/systemd/system/deadwood-mebot.service
```