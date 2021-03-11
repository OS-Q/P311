from SCons.Script import Import

Import("env")

env.Append(
    CCFLAGS=[
        "-Os",
        "-Wall",  # show warnings
        "-ffunction-sections",
        "-fdata-sections",
        "-fno-common"
    ],

    LINKFLAGS=[
        "-Os",
        "-ffunction-sections",
        "-fdata-sections",
        "-fno-common",
        "-Wl,--gc-sections"
    ],

    LIBS=[],
)

# copy CCFLAGS to ASFLAGS (-x assembler-with-cpp mode)
env.Append(ASFLAGS=env.get("CCFLAGS", [])[:])
