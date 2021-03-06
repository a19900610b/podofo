{
    'targets':[{
        "target_name" : "podofo",
        "type" : "static_library",
        "sources" : [
            "src/doc/PdfFontFactoryBase14Data.h",
            "src/doc/PdfAcroForm.cpp",
            "src/doc/PdfFontConfigWrapper.cpp",
            "src/doc/PdfMemDocument.cpp",
            "src/doc/PdfAction.cpp",
            "src/doc/PdfFontFactory.cpp",
            "src/doc/PdfNamesTree.cpp",
            "src/doc/PdfAnnotation.cpp",
            "src/doc/PdfFontMetrics.cpp",
            "src/doc/PdfOutlines.cpp",
            "src/doc/PdfCMapEncoding.cpp",
            "src/doc/PdfFontMetricsBase14.cpp",
            "src/doc/PdfPage.cpp",
            "src/doc/PdfContents.cpp",
            "src/doc/PdfFontMetricsFreetype.cpp",
            "src/doc/PdfPagesTree.cpp",
            "src/doc/PdfDestination.cpp",
            "src/doc/PdfFontMetricsObject.cpp",
            "src/doc/PdfPagesTreeCache.cpp",
            "src/doc/PdfDifferenceEncoding.cpp",
            "src/doc/PdfFontSimple.cpp",
            "src/doc/PdfPainter.cpp",
            "src/doc/PdfDocument.cpp",
            "src/doc/PdfFontTTFSubset.cpp",
            "src/doc/PdfPainterMM.cpp",
            "src/doc/PdfElement.cpp",
            "src/doc/PdfFontTrueType.cpp",
            "src/doc/PdfShadingPattern.cpp",
            "src/doc/PdfEncodingObjectFactory.cpp",
            "src/doc/PdfFontType1.cpp",
            "src/doc/PdfSignOutputDevice.cpp",
            "src/doc/PdfExtGState.cpp",
            "src/doc/PdfFontType1Base14.cpp",
            "src/doc/PdfSignatureField.cpp",
            "src/doc/PdfField.cpp",
            "src/doc/PdfFunction.cpp",
            "src/doc/PdfStreamedDocument.cpp",
            "src/doc/PdfFileSpec.cpp",
            "src/doc/PdfHintStream.cpp",
            "src/doc/PdfFont.cpp",
            "src/doc/PdfIdentityEncoding.cpp",
            "src/doc/PdfTable.cpp",
            "src/doc/PdfFontCID.cpp",
            "src/doc/PdfImage.cpp",
            "src/doc/PdfXObject.cpp",
            "src/doc/PdfFontCache.cpp",
            "src/doc/PdfInfo.cpp",
            "src/base/PdfArray.cpp",
            "src/base/PdfFiltersPrivate.cpp",
            "src/base/PdfRect.cpp",
            "src/base/PdfCanvas.cpp",
            "src/base/PdfImmediateWriter.cpp",
            "src/base/PdfRefCountedBuffer.cpp",
            "src/base/PdfColor.cpp",
            "src/base/PdfInputDevice.cpp",
            "src/base/PdfRefCountedInputDevice.cpp",
            "src/base/PdfContentsTokenizer.cpp",
            "src/base/PdfInputStream.cpp",
            "src/base/PdfReference.cpp",
            "src/base/PdfData.cpp",
            "src/base/PdfLocale.cpp",
            "src/base/PdfRijndael.cpp",
            "src/base/PdfDataType.cpp",
            "src/base/PdfMemStream.cpp",
            "src/base/PdfStream.cpp",
            "src/base/PdfDate.cpp",
            "src/base/PdfMemoryManagement.cpp",
            "src/base/PdfString.cpp",
            "src/base/PdfDictionary.cpp",
            "src/base/PdfName.cpp",
            "src/base/PdfTokenizer.cpp",
            "src/base/PdfEncoding.cpp",
            "src/base/PdfObject.cpp",
            "src/base/PdfVariant.cpp",
            "src/base/PdfEncodingFactory.cpp",
            "src/base/PdfObjectStreamParserObject.cpp",
            "src/base/PdfVecObjects.cpp",
            "src/base/PdfEncrypt.cpp",
            "src/base/PdfOutputDevice.cpp",
            "src/base/PdfWriter.cpp",
            "src/base/PdfError.cpp",
            "src/base/PdfOutputStream.cpp",
            "src/base/PdfXRef.cpp",
            "src/base/PdfFileStream.cpp",
            "src/base/PdfParser.cpp",
            "src/base/PdfXRefStream.cpp",
            "src/base/PdfFilter.cpp",
            "src/base/PdfParserObject.cpp",
            "src/base/PdfXRefStreamParserObject.cpp"],

        "include_dirs" :
           ["External/freetype/include",
            "./",
            "src",
            "src/base",
            "src/doc",
            "podofo-staticlib-osx/podofo/podofo" ],

        "conditions" : [
            ['OS=="mac"',
                { "cflags_cc!": [ "-fno-exceptions" ],
                "xcode_settings": {
                'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
                'GCC_ENABLE_CPP_RTTI': 'YES',
                'OTHER_CPLUSPLUSFLAGS' : ['-std=c++11','-stdlib=libc++'],
                'MACOSX_DEPLOYMENT_TARGET': '10.7'
                }
            }],
            ['OS=="linux"', {
                "cflags_cc!" : [ "-fno-exceptions", "-fno-rtti" ],
                "cflags_cc"  : [ "-std=c++0x" ]
            }]
        ],
        "link_settings" : { "libraries" : [ "-lz" ] },
        'defines' : [ 'BUILDING_PODOFO', 'PODOFO_HAVE_FREETYPE', 'DEBUG_PODOFO' ],
        'dependencies' : ['External/freetype/binding.gyp:freetype']
    }]
}
