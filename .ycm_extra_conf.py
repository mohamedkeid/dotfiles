def FlagsForFile(filename, **kwargs):
    return {
        'flags': [
            '-std=c++17', '-Wall', '-Wextra', '-Werror', '-I',
            '/usr/local/include', '-I', '/usr/local/include/gtest', '-isystem',
            '-I', '-I./include',
            '/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1',
            '-isystem',
            '/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/clang/10.0.0/include',
            '-isystem',
            '/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include',
            '-isystem',
            '/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk/usr/include'
        ],
        'do_cache':
        False
    }
