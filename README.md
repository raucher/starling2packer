# starling2packer
Python3 converter of starling XML texture-atlas format (widely used by [Kenny](https://kenney.nl/)) to Packer used by LibGDX

## Usage
`python3 starling2packer.py atlas_filename.xml`
will produce atlas_filename.pack file in Packer format

## Brief format differences overview
*Starling format:*
```xml
<TextureAtlas imagePath="shipsMiscellaneous_sheet.png">
  <SubTexture name="cannon.png" x="88" y="422" width="29" height="16"/>
  <SubTexture name="cannonBall.png" x="120" y="29" width="10" height="10"/>
</TextureAtlas>
```
*Packer format:*
```
shipsMiscellaneous_sheet.png
format: RGBA8888
filter: Linear,Linear
repeat: none
cannon.png
  rotate: false
  xy: 88, 422
  size: 29, 16
  orig: 29, 16
  offset: 0, 0
  index: -1
cannonBall.png
  rotate: false
  xy: 120, 29
  size: 10, 10
  orig: 10, 10
  offset: 0, 0
  index: -1
```
Converter uses corresponding <SubTexture ...> attributes names in string templates and populates them with node values. So templates can be easily modified if formats will change in the future.
Atlas example was taken from gorgeous https://kenney.nl/, happy coding :)
