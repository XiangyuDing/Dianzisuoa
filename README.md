# Dianzisuoa
ECE 1160 Embedded System Design - University of Pittsburgh

## API Audio to Text

Requires audio file of format:
    - OGG
    - FLAC

`nodejs audioToText <pathToAudioFile> [-json|-xml] [-file=pathToFile]`

Writes to standard out or file json or xml:
`[{message:"Text"}]`

`<message>Text</message>`

Default is json to standard out.
