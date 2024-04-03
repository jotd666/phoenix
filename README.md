# phoenix500
remake of Phoenix for Amiga

todo:

reverse functions of jump_table_040E
jump table? 0EE5


TILE_GET_INFO_MEMBER(phoenix_state::get_fg_tile_info)
{
	int code, col;

	code = m_videoram_pg[m_videoram_pg_index][tile_index];
	col = (code >> 5);
	col = col | 0x08 | (m_palette_bank << 4);
	tileinfo.set(1,
			code,
			col,
			0);
}

TILE_GET_INFO_MEMBER(phoenix_state::get_bg_tile_info)
{
	int code, col;

	code = m_videoram_pg[m_videoram_pg_index][tile_index + 0x800];
	col = (code >> 5);
	col = col | 0x00 | (m_palette_bank << 4);
	tileinfo.set(0,
			code,
			col,
			0);
}
