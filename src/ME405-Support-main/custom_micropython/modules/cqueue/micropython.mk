
BERFMODS_DIR := $(USERMOD_DIR)

# Add all C files to SRC_USERMOD.
SRC_USERMOD += $(BERFMODS_DIR)/cqueue.c

CFLAGS_USERMOD += -I$(BERFMODS_DIR)

override CFLAGS_EXTRA += -DMODULE_BERF_ENABLED=1
