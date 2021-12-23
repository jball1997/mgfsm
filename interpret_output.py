codebook = {'assertion': 0,
            'bench_get': 1,
            'bench_to_fixture': 2,
            'bluej_finish': 3,
            'bluej_start': 4,
            'cancel_test': 5,
            'code_completion_ended': 6,
            'code_completion_started': 7,
            'codepad': 8,
            'compile': 9,
            'convert_java_to_stride': 10,
            'convert_stride_to_java': 11,
            'debugger_breakpoint_add': 12,
            'debugger_breakpoint_remove': 13,
            'debugger_close': 14,
            'debugger_continue': 15,
            'debugger_halt': 16,
            'debugger_hit_breakpoint': 17,
            'debugger_open': 18,
            'debugger_stepinto': 19,
            'debugger_stepover': 20,
            'debugger_terminate': 21,
            'edit': 22,
            'end_test': 23,
            'file_add': 24,
            'file_close': 25,
            'file_delete': 26,
            'file_open': 27,
            'file_select': 28,
            'fix_executed': 29,
            'fixture_to_bench': 30,
            'frame_catalogue_showing': 31,
            'greenfoot_window_activated': 32,
            'greenfoot_world_act': 33,
            'greenfoot_world_pause': 34,
            'greenfoot_world_reset': 35,
            'greenfoot_world_run': 36,
            'inspector_hide': 37,
            'inspector_show': 38,
            'invoke_method': 39,
            'package_closing': 40,
            'package_opening': 41,
            'project_closing': 42,
            'project_opening': 43,
            'remove_object': 44,
            'rename': 45,
            'resetting_vm': 46,
            'run_test': 47,
            'shown_error_indicator': 48,
            'shown_error_message': 49,
            'start_test': 50,
            'terminal_close': 51,
            'terminal_open': 52,
            'unknown_frame_command': 53,
            'vcs_commit': 54,
            'vcs_history': 55,
            'vcs_push': 56,
            'vcs_share': 57,
            'vcs_status': 58,
            'vcs_update': 59,
            'view_mode_change': 60
            }

# flipping codebook
flipped_codebook = {}
for key, val in codebook.items():
  flipped_codebook[str(val)] = key

# duplicating patterns with readable names
with open('OUTPUT/translatedFS') as fin:
    patterns = fin.read().split('\n')[:-1]
    # print(repr(patterns[0]))
    for pattern_i, pattern in enumerate(patterns):
        pattern = pattern.split()
        frequency = pattern[-1]
        pattern = pattern[:-1]
        # convert to names of events
        for event_i in range(len(pattern)):
            pattern[event_i] = flipped_codebook[pattern[event_i]]
        # replace
        patterns[pattern_i] = ' '.join(pattern) + ' \t' + frequency + '\n'
    # print(patterns[:2])
    with open('OUTPUT/ReadableTranslatedFS', 'w') as fout:
        fout.writelines(patterns)
