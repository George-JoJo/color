# color

## BT.709 -> BT.601 转换

已实现 `Y'CbCr` 码值从 **BT.709** 到 **BT.601** 的矩阵转换（通过 `R'G'B'` 中间域）：

- 入口函数：`convert_bt709_to_bt601(y, cb, cr, bit_depth=8, range_mode="limited")`
- 文件位置：`color_conversion.py`
- 支持范围：
  - `range_mode="limited"`（TV range）
  - `range_mode="full"`（Full range）
- 支持任意 `bit_depth >= 8`（常见 8/10bit）

### 命令行示例

```bash
python color_conversion.py --y 100 --cb 150 --cr 200 --bit-depth 8 --range-mode limited
```

输出格式：`Y,Cb,Cr`

### 运行测试

```bash
python -m unittest discover -s tests -v
```