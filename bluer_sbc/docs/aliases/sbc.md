# aliases: sbc


# parts
```bash
@parts \
	adjust \
	[dryrun,~grid] \
	[--verbose 1]
 . adjust part images.
@parts \
	cd
 . cd to part images folder.
@parts \
	edit
 . edit parts db.
@parts \
	open
 . open part images folder.
```

# rpi
```bash
@sbc \
	rpi \
	fake_display \
	[dryrun]
 . fake the display on an rpi.
```
