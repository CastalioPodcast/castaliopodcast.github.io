help:
	@echo 'Makefile for utility scripts                                              '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make stats                          Display download stats             '
	@echo '   make top5stats                      Build global top5 stats data file  '
	@echo '                                                                          '

stats:
	./scripts/stats.py content/episodes/*.rst

top5stats:
	./scripts/top5stats.py content/episodes/ data/

.PHONY: help stats top5stats
