class InputSource:
    """Tracks the line number as we iterate over lines of text."""
    _lines: List[str]
    _base_line_number: int

    def __init__(self, text: str, base_line_number=0):
        self._base_line_number = base_line_number
        self._lines = [l.strip() for l in text.split('\n')]

    def __getitem__(self, index) -> str:
        return self._lines[index]

    def __len__(self) -> int:
        return len(self._lines)

    def line_number(self) -> int:
        return self._base_line_number

    def consume(self, n=1) -> None:
        self._lines = self._lines[n:]
        self._base_line_number += n

    """A line of text that tracks its line number."""
    def __init__(self, line_number: int, text: str) -> None:
    def __init__(self, parent_line_number: int, child_line_number: int, text: str) -> None:
    def __init__(self, last_parent_line_number: int, child_line_number: int, text: str) -> None:
    for i, line in enumerate(text.splitlines()):
        line_list.append(Line(text=line, line_number=i))
    patch_list.sort(key=lambda x: x.set_index)
def _does_match_end_of_super_chunk(lines: InputSource) -> bool:
        lines: InputSource,
        gerrit_new_line: int) -> Tuple[int, int, PatchFileChunkLineMap]:
    in_start = lines.line_number()
        lines.consume()
            PatchFileChunkLineMap(in_range=(in_start, lines.line_number() - 1),
                                  offset=(gerrit_new_line - lines.line_number())))
        lines: InputSource,
        gerrit_new_line: int) -> Tuple[int, int, PatchFileChunkLineMap]:
    in_start = lines.line_number()
        lines.consume()
            PatchFileChunkLineMap(in_range=(in_start, lines.line_number() - 1),
                                  offset=(gerrit_new_line - lines.line_number())))
        lines: InputSource,
        gerrit_new_line: int) -> Tuple[int, int, PatchFileChunkLineMap]:
    in_start = lines.line_number()
        lines.consume()
            PatchFileChunkLineMap(in_range=(in_start, lines.line_number() - 1),
                                  offset=(gerrit_new_line - lines.line_number())))
def _parse_patch_file_chunk(lines: InputSource,
                            gerrit_new_line: int) -> Tuple[int, int, PatchFileChunkLineMap]:
        ret_val =  _parse_patch_file_added_chunk(lines, gerrit_orig_line, gerrit_new_line)
        ret_val = _parse_patch_file_removed_chunk(lines, gerrit_orig_line, gerrit_new_line)
        ret_val = _parse_patch_file_unchanged_chunk(lines, gerrit_orig_line, gerrit_new_line)
def _parse_patch_file_super_chunk(lines: InputSource) -> List[PatchFileChunkLineMap]:

    lines.consume()
def _parse_patch_file_entry(lines: InputSource) -> Optional[PatchFileLineMap]:
    lines.consume()
        lines.consume()
        lines.consume()
        lines.consume()
        lines.consume()
    old_index = lines.line_number()
    super_chunk = _parse_patch_file_super_chunk(lines)
        logging.info('parsed super chunk: %d to %d', old_index, chunk.in_range[1])
        old_index = lines.line_number()
        super_chunk = _parse_patch_file_super_chunk(lines)
def _find_diff_start(lines: InputSource) -> None:
            lines.consume(i)
        lines.consume()
        lines.consume()
        lines.consume()
        lines.consume()
        lines.consume()
    if not DIFF_LINE_MATCHER.match(lines[0]):
    lines = InputSource(raw_patch)
    _find_diff_start(lines)
    file_entry = _parse_patch_file_entry(lines)
        file_entry = _parse_patch_file_entry(lines)
        raise ValueError(f'Could not parse entire file: error at line {lines.line_number()}: ' + lines[0])