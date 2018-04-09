RUN_CMD := python hello.py

run:
	$(RUN_CMD)

cf:
	cf push prerequisite -c '$(RUN_CMD)'
