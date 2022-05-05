import QtQuick
import QtQuick.Controls.Basic
ApplicationWindow {
    visible: true
    width: 600
    height: 500
    title: "Hello Desktop Application"
    Text {
        anchor.centerIm: parent
        text: "Hello Application"
        font.pixelSize: 24
    }
}