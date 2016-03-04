{
  "variables": {
    "pdf_enable_v8%": 1,
  },
  "target_defaults": {
    "defines": [
      "PDF_ENABLE_XFA",
    ],
    'msvs_disabled_warnings': [
      4005, 4018, 4146, 4333, 4345, 4267,
      # TODO(thestig): Fix all instances, remove this, pdfium:29
      4245, 4310, 4389, 4701, 4702, 4706, 4800,
    ],
  },
  "targets":[
    {
      "target_name":"xfa",
      "type":"static_library",
      'include_dirs': [
        # This is implicit in GN.
        '<(DEPTH)',
        '.',
        'third_party/freetype/include',
        'third_party/freetype/include/freetype',
      ],
      'defines' : [
        'FT2_BUILD_LIBRARY',
      ],
      "sources":[
        "xfa/include/fwl/adapter/fwl_adapternative.h",
        "xfa/include/fwl/adapter/fwl_adapterthreadmgr.h",
        "xfa/include/fwl/adapter/fwl_adaptertimermgr.h",
        "xfa/include/fwl/adapter/fwl_adapterwidgetmgr.h",
        "xfa/include/fwl/adapter/fwl_sdadapterimp.h",
        "xfa/include/fwl/basewidget/fwl_barcode.h",
        "xfa/include/fwl/basewidget/fwl_caret.h",
        "xfa/include/fwl/basewidget/fwl_checkbox.h",
        "xfa/include/fwl/basewidget/fwl_combobox.h",
        "xfa/include/fwl/basewidget/fwl_datetimepicker.h",
        "xfa/include/fwl/basewidget/fwl_edit.h",
        "xfa/include/fwl/basewidget/fwl_listbox.h",
        "xfa/include/fwl/basewidget/fwl_menu.h",
        "xfa/include/fwl/basewidget/fwl_monthcalendar.h",
        "xfa/include/fwl/basewidget/fwl_picturebox.h",
        "xfa/include/fwl/basewidget/fwl_pushbutton.h",
        "xfa/include/fwl/basewidget/fwl_scrollbar.h",
        "xfa/include/fwl/basewidget/fwl_spinbutton.h",
        "xfa/include/fwl/basewidget/fwl_tooltipctrl.h",
        "xfa/include/fwl/basewidget/fxmath_barcode.h",
        "xfa/include/fwl/core/fwl_app.h",
        "xfa/include/fwl/core/fwl_content.h",
        "xfa/include/fwl/core/fwl_error.h",
        "xfa/include/fwl/core/fwl_form.h",
        "xfa/include/fwl/core/fwl_grid.h",
        "xfa/include/fwl/core/fwl_note.h",
        "xfa/include/fwl/core/fwl_panel.h",
        "xfa/include/fwl/core/fwl_target.h",
        "xfa/include/fwl/core/fwl_theme.h",
        "xfa/include/fwl/core/fwl_thread.h",
        "xfa/include/fwl/core/fwl_timer.h",
        "xfa/include/fwl/core/fwl_widget.h",
        "xfa/include/fwl/core/fwl_widgetdef.h",
        "xfa/include/fwl/core/fwl_widgetmgr.h",
        "xfa/include/fwl/lightwidget/app.h",
        "xfa/include/fwl/lightwidget/barcode.h",
        "xfa/include/fwl/lightwidget/caret.h",
        "xfa/include/fwl/lightwidget/checkbox.h",
        "xfa/include/fwl/lightwidget/combobox.h",
        "xfa/include/fwl/lightwidget/datetimepicker.h",
        "xfa/include/fwl/lightwidget/edit.h",
        "xfa/include/fwl/lightwidget/listbox.h",
        "xfa/include/fwl/lightwidget/picturebox.h",
        "xfa/include/fwl/lightwidget/pushbutton.h",
        "xfa/include/fwl/lightwidget/scrollbar.h",
        "xfa/include/fwl/lightwidget/theme.h",
        "xfa/include/fwl/lightwidget/tooltipctrl.h",
        "xfa/include/fwl/lightwidget/widget.h",
        "xfa/include/fwl/theme/barcodetp.h",
        "xfa/include/fwl/theme/carettp.h",
        "xfa/include/fwl/theme/checkboxtp.h",
        "xfa/include/fwl/theme/comboboxtp.h",
        "xfa/include/fwl/theme/datetimepickertp.h",
        "xfa/include/fwl/theme/edittp.h",
        "xfa/include/fwl/theme/formtp.h",
        "xfa/include/fwl/theme/listboxtp.h",
        "xfa/include/fwl/theme/monthcalendartp.h",
        "xfa/include/fwl/theme/pictureboxtp.h",
        "xfa/include/fwl/theme/pushbuttontp.h",
        "xfa/include/fwl/theme/scrollbartp.h",
        "xfa/include/fwl/theme/utils.h",
        "xfa/include/fwl/theme/widgettp.h",
        "xfa/include/fxbarcode/BC_BarCode.h",
        "xfa/include/fxfa/fxfa.h",
        "xfa/include/fxfa/fxfa_basic.h",
        "xfa/include/fxfa/fxfa_objectacc.h",
        "xfa/include/fxfa/fxfa_widget.h",
        "xfa/include/fxgraphics/fx_graphics.h",
        "xfa/include/fxjse/fxjse.h",
        "xfa/src/fdp/include/fde_brs.h",
        "xfa/src/fdp/include/fde_css.h",
        "xfa/src/fdp/include/fde_img.h",
        "xfa/src/fdp/include/fde_pen.h",
        "xfa/src/fdp/include/fde_psr.h",
        "xfa/src/fdp/include/fde_pth.h",
        "xfa/src/fdp/include/fde_rdr.h",
        "xfa/src/fdp/include/fde_rdv.h",
        "xfa/src/fdp/include/fde_tto.h",
        "xfa/src/fdp/include/fde_xml.h",
        "xfa/src/fdp/src/css/fde_csscache.cpp",
        "xfa/src/fdp/src/css/fde_csscache.h",
        "xfa/src/fdp/src/css/fde_cssdatatable.cpp",
        "xfa/src/fdp/src/css/fde_cssdatatable.h",
        "xfa/src/fdp/src/css/fde_cssdeclaration.cpp",
        "xfa/src/fdp/src/css/fde_cssdeclaration.h",
        "xfa/src/fdp/src/css/fde_cssstyleselector.cpp",
        "xfa/src/fdp/src/css/fde_cssstyleselector.h",
        "xfa/src/fdp/src/css/fde_cssstylesheet.cpp",
        "xfa/src/fdp/src/css/fde_cssstylesheet.h",
        "xfa/src/fdp/src/css/fde_csssyntax.cpp",
        "xfa/src/fdp/src/css/fde_csssyntax.h",
        "xfa/src/fdp/src/fde/fde_devbasic.cpp",
        "xfa/src/fdp/src/fde/fde_devbasic.h",
        "xfa/src/fdp/src/fde/fde_gedevice.cpp",
        "xfa/src/fdp/src/fde/fde_gedevice.h",
        "xfa/src/fdp/src/fde/fde_geobject.cpp",
        "xfa/src/fdp/src/fde/fde_geobject.h",
        "xfa/src/fdp/src/fde/fde_iterator.cpp",
        "xfa/src/fdp/src/fde/fde_iterator.h",
        "xfa/src/fdp/src/fde/fde_object.cpp",
        "xfa/src/fdp/src/fde/fde_object.h",
        "xfa/src/fdp/src/fde/fde_render.cpp",
        "xfa/src/fdp/src/fde/fde_render.h",
        "xfa/src/fdp/src/tto/fde_textout.cpp",
        "xfa/src/fdp/src/tto/fde_textout.h",
        "xfa/src/fdp/src/xml/fde_xml_imp.cpp",
        "xfa/src/fdp/src/xml/fde_xml_imp.h",
        "xfa/src/fee/include/fx_wordbreak.h",
        "xfa/src/fee/include/ifde_txtedtbuf.h",
        "xfa/src/fee/include/ifde_txtedtengine.h",
        "xfa/src/fee/include/ifde_txtedtpage.h",
        "xfa/src/fee/src/fee/fde_txtedtbuf.cpp",
        "xfa/src/fee/src/fee/fde_txtedtbuf.h",
        "xfa/src/fee/src/fee/fde_txtedtengine.cpp",
        "xfa/src/fee/src/fee/fde_txtedtengine.h",
        "xfa/src/fee/src/fee/fde_txtedtpage.cpp",
        "xfa/src/fee/src/fee/fde_txtedtpage.h",
        "xfa/src/fee/src/fee/fde_txtedtparag.cpp",
        "xfa/src/fee/src/fee/fde_txtedtparag.h",
        "xfa/src/fee/src/fx_wordbreak/fx_wordbreakdata.cpp",
        "xfa/src/fee/src/fx_wordbreak/fx_wordbreak_impl.cpp",
        "xfa/src/fee/src/fx_wordbreak/fx_wordbreak_impl.h",
        "xfa/src/fgas/include/fx_alg.h",
        "xfa/src/fgas/include/fx_cpg.h",
        "xfa/src/fgas/include/fx_datetime.h",
        "xfa/src/fgas/include/fx_fnt.h",
        "xfa/src/fgas/include/fx_lbk.h",
        "xfa/src/fgas/include/fx_lgg.h",
        "xfa/src/fgas/include/fx_locale.h",
        "xfa/src/fgas/include/fx_mem.h",
        "xfa/src/fgas/include/fx_rbk.h",
        "xfa/src/fgas/include/fx_sax.h",
        "xfa/src/fgas/include/fx_stm.h",
        "xfa/src/fgas/include/fx_sys.h",
        "xfa/src/fgas/include/fx_tbk.h",
        "xfa/src/fgas/include/fx_ucd.h",
        "xfa/src/fgas/include/fx_utl.h",
        "xfa/src/fgas/src/crt/fx_algorithm.cpp",
        "xfa/src/fgas/src/crt/fx_codepage.cpp",
        "xfa/src/fgas/src/crt/fx_encode.cpp",
        "xfa/src/fgas/src/crt/fx_memory.cpp",
        "xfa/src/fgas/src/crt/fx_memory.h",
        "xfa/src/fgas/src/crt/fx_stream.cpp",
        "xfa/src/fgas/src/crt/fx_stream.h",
        "xfa/src/fgas/src/crt/fx_system.cpp",
        "xfa/src/fgas/src/crt/fx_utils.cpp",
        "xfa/src/fgas/src/crt/fx_utils.h",
        "xfa/src/fgas/src/font/fx_fontutils.cpp",
        "xfa/src/fgas/src/font/fx_fontutils.h",
        "xfa/src/fgas/src/font/fx_gefont.cpp",
        "xfa/src/fgas/src/font/fx_gefont.h",
        "xfa/src/fgas/src/font/fx_stdfontmgr.cpp",
        "xfa/src/fgas/src/font/fx_stdfontmgr.h",
        "xfa/src/fgas/src/layout/fx_linebreak.cpp",
        "xfa/src/fgas/src/layout/fx_rtfbreak.cpp",
        "xfa/src/fgas/src/layout/fx_rtfbreak.h",
        "xfa/src/fgas/src/layout/fx_textbreak.cpp",
        "xfa/src/fgas/src/layout/fx_textbreak.h",
        "xfa/src/fgas/src/layout/fx_unicode.cpp",
        "xfa/src/fgas/src/layout/fx_unicode.h",
        "xfa/src/fgas/src/localization/fx_datetime.cpp",
        "xfa/src/fgas/src/localization/fx_locale.cpp",
        "xfa/src/fgas/src/localization/fx_localeimp.h",
        "xfa/src/fgas/src/localization/fx_localemgr.cpp",
        "xfa/src/fgas/src/localization/fx_localemgr.h",
        "xfa/src/fgas/src/xml/fx_sax_imp.cpp",
        "xfa/src/fgas/src/xml/fx_sax_imp.h",
        "xfa/src/fwl/src/basewidget/fwl_barcodeimp.cpp",
        "xfa/src/fwl/src/basewidget/fwl_caretimp.cpp",
        "xfa/src/fwl/src/basewidget/fwl_checkboximp.cpp",
        "xfa/src/fwl/src/basewidget/fwl_comboboximp.cpp",
        "xfa/src/fwl/src/basewidget/fwl_datetimepickerimp.cpp",
        "xfa/src/fwl/src/basewidget/fwl_editimp.cpp",
        "xfa/src/fwl/src/basewidget/fwl_formproxyimp.cpp",
        "xfa/src/fwl/src/basewidget/fwl_listboximp.cpp",
        "xfa/src/fwl/src/basewidget/fwl_monthcalendarimp.cpp",
        "xfa/src/fwl/src/basewidget/fwl_pictureboximp.cpp",
        "xfa/src/fwl/src/basewidget/fwl_pushbuttonimp.cpp",
        "xfa/src/fwl/src/basewidget/fwl_scrollbarimp.cpp",
        "xfa/src/fwl/src/basewidget/fwl_spinbuttonimp.cpp",
        "xfa/src/fwl/src/basewidget/fwl_tooltipctrlimp.cpp",
        "xfa/src/fwl/src/basewidget/fxmath_barcodeimp.cpp",
        "xfa/src/fwl/src/basewidget/include/fwl_barcodeimp.h",
        "xfa/src/fwl/src/basewidget/include/fwl_caretimp.h",
        "xfa/src/fwl/src/basewidget/include/fwl_checkboximp.h",
        "xfa/src/fwl/src/basewidget/include/fwl_comboboximp.h",
        "xfa/src/fwl/src/basewidget/include/fwl_datetimepickerimp.h",
        "xfa/src/fwl/src/basewidget/include/fwl_editimp.h",
        "xfa/src/fwl/src/basewidget/include/fwl_formproxyimp.h",
        "xfa/src/fwl/src/basewidget/include/fwl_listboximp.h",
        "xfa/src/fwl/src/basewidget/include/fwl_monthcalendarimp.h",
        "xfa/src/fwl/src/basewidget/include/fwl_pictureboximp.h",
        "xfa/src/fwl/src/basewidget/include/fwl_pushbuttonimp.h",
        "xfa/src/fwl/src/basewidget/include/fwl_scrollbarimp.h",
        "xfa/src/fwl/src/basewidget/include/fwl_spinbuttonimp.h",
        "xfa/src/fwl/src/basewidget/include/fwl_tooltipctrlimp.h",
        "xfa/src/fwl/src/basewidget/include/fxmath_barcodeimp.h",
        "xfa/src/fwl/src/core/fwl_appimp.cpp",
        "xfa/src/fwl/src/core/fwl_contentimp.cpp",
        "xfa/src/fwl/src/core/fwl_formimp.cpp",
        "xfa/src/fwl/src/core/fwl_gridimp.cpp",
        "xfa/src/fwl/src/core/fwl_noteimp.cpp",
        "xfa/src/fwl/src/core/fwl_panelimp.cpp",
        "xfa/src/fwl/src/core/fwl_sdadapterimp.cpp",
        "xfa/src/fwl/src/core/fwl_targetimp.cpp",
        "xfa/src/fwl/src/core/fwl_threadimp.cpp",
        "xfa/src/fwl/src/core/fwl_timerimp.cpp",
        "xfa/src/fwl/src/core/fwl_widgetimp.cpp",
        "xfa/src/fwl/src/core/fwl_widgetmgrimp.cpp",
        "xfa/src/fwl/src/core/include/fwl_appimp.h",
        "xfa/src/fwl/src/core/include/fwl_contentimp.h",
        "xfa/src/fwl/src/core/include/fwl_formimp.h",
        "xfa/src/fwl/src/core/include/fwl_gridimp.h",
        "xfa/src/fwl/src/core/include/fwl_noteimp.h",
        "xfa/src/fwl/src/core/include/fwl_panelimp.h",
        "xfa/src/fwl/src/core/include/fwl_targetimp.h",
        "xfa/src/fwl/src/core/include/fwl_threadimp.h",
        "xfa/src/fwl/src/core/include/fwl_widgetimp.h",
        "xfa/src/fwl/src/core/include/fwl_widgetmgrimp.h",
        "xfa/src/fwl/src/lightwidget/app.cpp",
        "xfa/src/fwl/src/lightwidget/barcode.cpp",
        "xfa/src/fwl/src/lightwidget/caret.cpp",
        "xfa/src/fwl/src/lightwidget/checkbox.cpp",
        "xfa/src/fwl/src/lightwidget/combobox.cpp",
        "xfa/src/fwl/src/lightwidget/datetimepicker.cpp",
        "xfa/src/fwl/src/lightwidget/edit.cpp",
        "xfa/src/fwl/src/lightwidget/listbox.cpp",
        "xfa/src/fwl/src/lightwidget/picturebox.cpp",
        "xfa/src/fwl/src/lightwidget/pushbutton.cpp",
        "xfa/src/fwl/src/lightwidget/scrollbar.cpp",
        "xfa/src/fwl/src/lightwidget/theme.cpp",
        "xfa/src/fwl/src/lightwidget/tooltipctrl.cpp",
        "xfa/src/fwl/src/lightwidget/widget.cpp",
        "xfa/src/fwl/src/theme/barcodetp.cpp",
        "xfa/src/fwl/src/theme/carettp.cpp",
        "xfa/src/fwl/src/theme/checkboxtp.cpp",
        "xfa/src/fwl/src/theme/comboboxtp.cpp",
        "xfa/src/fwl/src/theme/datetimepickertp.cpp",
        "xfa/src/fwl/src/theme/edittp.cpp",
        "xfa/src/fwl/src/theme/formtp.cpp",
        "xfa/src/fwl/src/theme/listboxtp.cpp",
        "xfa/src/fwl/src/theme/monthcalendartp.cpp",
        "xfa/src/fwl/src/theme/pictureboxtp.cpp",
        "xfa/src/fwl/src/theme/pushbuttontp.cpp",
        "xfa/src/fwl/src/theme/scrollbartp.cpp",
        "xfa/src/fwl/src/theme/widgettp.cpp",
        "xfa/src/fxbarcode/common/BC_CommonBitArray.cpp",
        "xfa/src/fxbarcode/common/BC_CommonBitMatrix.cpp",
        "xfa/src/fxbarcode/common/BC_CommonBitSource.cpp",
        "xfa/src/fxbarcode/common/BC_CommonByteArray.cpp",
        "xfa/src/fxbarcode/common/BC_CommonByteMatrix.cpp",
        "xfa/src/fxbarcode/common/BC_CommonCharacterSetECI.cpp",
        "xfa/src/fxbarcode/common/BC_CommonDecoderResult.cpp",
        "xfa/src/fxbarcode/common/BC_CommonECI.cpp",
        "xfa/src/fxbarcode/common/BC_CommonPerspectiveTransform.cpp",
        "xfa/src/fxbarcode/common/BC_CommonBitArray.h",
        "xfa/src/fxbarcode/common/BC_CommonBitMatrix.h",
        "xfa/src/fxbarcode/common/BC_CommonBitSource.h",
        "xfa/src/fxbarcode/common/BC_CommonByteArray.h",
        "xfa/src/fxbarcode/common/BC_CommonByteMatrix.h",
        "xfa/src/fxbarcode/common/BC_CommonCharacterSetECI.h",
        "xfa/src/fxbarcode/common/BC_CommonDecoderResult.h",
        "xfa/src/fxbarcode/common/BC_CommonECI.h",
        "xfa/src/fxbarcode/common/BC_CommonPerspectiveTransform.h",
        "xfa/src/fxbarcode/common/BC_WhiteRectangleDetector.cpp",
        "xfa/src/fxbarcode/common/BC_WhiteRectangleDetector.h",
        "xfa/src/fxbarcode/common/BC_GlobalHistogramBinarizer.cpp",
        "xfa/src/fxbarcode/common/BC_GlobalHistogramBinarizer.h",
        "xfa/src/fxbarcode/common/reedsolomon/BC_ReedSolomon.cpp",
        "xfa/src/fxbarcode/common/reedsolomon/BC_ReedSolomonDecoder.cpp",
        "xfa/src/fxbarcode/common/reedsolomon/BC_ReedSolomonGF256.cpp",
        "xfa/src/fxbarcode/common/reedsolomon/BC_ReedSolomonGF256Poly.cpp",
        "xfa/src/fxbarcode/common/reedsolomon/BC_ReedSolomon.h",
        "xfa/src/fxbarcode/common/reedsolomon/BC_ReedSolomonDecoder.h",
        "xfa/src/fxbarcode/common/reedsolomon/BC_ReedSolomonGF256.h",
        "xfa/src/fxbarcode/common/reedsolomon/BC_ReedSolomonGF256Poly.h",
        "xfa/src/fxbarcode/datamatrix/BC_DataMatrixBitMatrixParser.cpp",
        "xfa/src/fxbarcode/datamatrix/BC_DataMatrixDataBlock.cpp",
        "xfa/src/fxbarcode/datamatrix/BC_DataMatrixDecodedBitStreamParser.cpp",
        "xfa/src/fxbarcode/datamatrix/BC_DataMatrixDecoder.cpp",
        "xfa/src/fxbarcode/datamatrix/BC_DataMatrixDetector.cpp",
        "xfa/src/fxbarcode/datamatrix/BC_DataMatrixReader.cpp",
        "xfa/src/fxbarcode/datamatrix/BC_DataMatrixSymbolInfo144.cpp",
        "xfa/src/fxbarcode/datamatrix/BC_DataMatrixVersion.cpp",
        "xfa/src/fxbarcode/datamatrix/BC_DataMatrixWriter.cpp",
        "xfa/src/fxbarcode/datamatrix/BC_DataMatrixBitMatrixParser.h",
        "xfa/src/fxbarcode/datamatrix/BC_DataMatrixDataBlock.h",
        "xfa/src/fxbarcode/datamatrix/BC_DataMatrixDecodedBitStreamParser.h",
        "xfa/src/fxbarcode/datamatrix/BC_DataMatrixDecoder.h",
        "xfa/src/fxbarcode/datamatrix/BC_DataMatrixDetector.h",
        "xfa/src/fxbarcode/datamatrix/BC_DataMatrixReader.h",
        "xfa/src/fxbarcode/datamatrix/BC_DataMatrixSymbolInfo144.h",
        "xfa/src/fxbarcode/datamatrix/BC_DataMatrixVersion.h",
        "xfa/src/fxbarcode/datamatrix/BC_DataMatrixWriter.h",
        "xfa/src/fxbarcode/datamatrix/BC_ASCIIEncoder.cpp",
        "xfa/src/fxbarcode/datamatrix/BC_Base256Encoder.cpp",
        "xfa/src/fxbarcode/datamatrix/BC_C40Encoder.cpp",
        "xfa/src/fxbarcode/datamatrix/BC_EdifactEncoder.cpp",
        "xfa/src/fxbarcode/datamatrix/BC_EncoderContext.cpp",
        "xfa/src/fxbarcode/datamatrix/BC_ErrorCorrection.cpp",
        "xfa/src/fxbarcode/datamatrix/BC_SymbolInfo.cpp",
        "xfa/src/fxbarcode/datamatrix/BC_SymbolShapeHint.cpp",
        "xfa/src/fxbarcode/datamatrix/BC_TextEncoder.cpp",
        "xfa/src/fxbarcode/datamatrix/BC_X12Encoder.cpp",
        "xfa/src/fxbarcode/datamatrix/BC_DefaultPlacement.cpp",
        "xfa/src/fxbarcode/datamatrix/BC_Encoder.cpp",
        "xfa/src/fxbarcode/datamatrix/BC_HighLevelEncoder.cpp",
        "xfa/src/fxbarcode/datamatrix/BC_ASCIIEncoder.h",
        "xfa/src/fxbarcode/datamatrix/BC_Base256Encoder.h",
        "xfa/src/fxbarcode/datamatrix/BC_C40Encoder.h",
        "xfa/src/fxbarcode/datamatrix/BC_EdifactEncoder.h",
        "xfa/src/fxbarcode/datamatrix/BC_EncoderContext.h",
        "xfa/src/fxbarcode/datamatrix/BC_ErrorCorrection.h",
        "xfa/src/fxbarcode/datamatrix/BC_SymbolInfo.h",
        "xfa/src/fxbarcode/datamatrix/BC_SymbolShapeHint.h",
        "xfa/src/fxbarcode/datamatrix/BC_TextEncoder.h",
        "xfa/src/fxbarcode/datamatrix/BC_X12Encoder.h",
        "xfa/src/fxbarcode/datamatrix/BC_DefaultPlacement.h",
        "xfa/src/fxbarcode/datamatrix/BC_Encoder.h",
        "xfa/src/fxbarcode/datamatrix/BC_HighLevelEncoder.h",
        "xfa/src/fxbarcode/oned/BC_OnedCodaBarReader.cpp",
        "xfa/src/fxbarcode/oned/BC_OnedCodaBarWriter.cpp",
        "xfa/src/fxbarcode/oned/BC_OnedCode128Reader.cpp",
        "xfa/src/fxbarcode/oned/BC_OnedCode128Writer.cpp",
        "xfa/src/fxbarcode/oned/BC_OnedCode39Reader.cpp",
        "xfa/src/fxbarcode/oned/BC_OnedCode39Writer.cpp",
        "xfa/src/fxbarcode/oned/BC_OnedEAN13Reader.cpp",
        "xfa/src/fxbarcode/oned/BC_OnedEAN13Writer.cpp",
        "xfa/src/fxbarcode/oned/BC_OnedEAN8Reader.cpp",
        "xfa/src/fxbarcode/oned/BC_OnedEAN8Writer.cpp",
        "xfa/src/fxbarcode/oned/BC_OneDimReader.cpp",
        "xfa/src/fxbarcode/oned/BC_OneDimWriter.cpp",
        "xfa/src/fxbarcode/oned/BC_OneDReader.cpp",
        "xfa/src/fxbarcode/oned/BC_OnedUPCAReader.cpp",
        "xfa/src/fxbarcode/oned/BC_OnedUPCAWriter.cpp",
        "xfa/src/fxbarcode/oned/BC_OnedCodaBarReader.h",
        "xfa/src/fxbarcode/oned/BC_OnedCodaBarWriter.h",
        "xfa/src/fxbarcode/oned/BC_OnedCode128Reader.h",
        "xfa/src/fxbarcode/oned/BC_OnedCode128Writer.h",
        "xfa/src/fxbarcode/oned/BC_OnedCode39Reader.h",
        "xfa/src/fxbarcode/oned/BC_OnedCode39Writer.h",
        "xfa/src/fxbarcode/oned/BC_OnedEAN13Reader.h",
        "xfa/src/fxbarcode/oned/BC_OnedEAN13Writer.h",
        "xfa/src/fxbarcode/oned/BC_OnedEAN8Reader.h",
        "xfa/src/fxbarcode/oned/BC_OnedEAN8Writer.h",
        "xfa/src/fxbarcode/oned/BC_OneDimReader.h",
        "xfa/src/fxbarcode/oned/BC_OneDimWriter.h",
        "xfa/src/fxbarcode/oned/BC_OneDReader.h",
        "xfa/src/fxbarcode/oned/BC_OnedUPCAReader.h",
        "xfa/src/fxbarcode/oned/BC_OnedUPCAWriter.h",
        "xfa/src/fxbarcode/pdf417/BC_PDF417.cpp",
        "xfa/src/fxbarcode/pdf417/BC_PDF417BarcodeMatrix.cpp",
        "xfa/src/fxbarcode/pdf417/BC_PDF417BarcodeMetadata.cpp",
        "xfa/src/fxbarcode/pdf417/BC_PDF417BarcodeRow.cpp",
        "xfa/src/fxbarcode/pdf417/BC_PDF417BarcodeValue.cpp",
        "xfa/src/fxbarcode/pdf417/BC_PDF417BoundingBox.cpp",
        "xfa/src/fxbarcode/pdf417/BC_PDF417Codeword.cpp",
        "xfa/src/fxbarcode/pdf417/BC_PDF417CodewordDecoder.cpp",
        "xfa/src/fxbarcode/pdf417/BC_PDF417Common.cpp",
        "xfa/src/fxbarcode/pdf417/BC_PDF417Compaction.cpp",
        "xfa/src/fxbarcode/pdf417/BC_PDF417DecodedBitStreamParser.cpp",
        "xfa/src/fxbarcode/pdf417/BC_PDF417DetectionResult.cpp",
        "xfa/src/fxbarcode/pdf417/BC_PDF417DetectionResultColumn.cpp",
        "xfa/src/fxbarcode/pdf417/BC_PDF417DetectionResultRowIndicatorColumn.cpp",
        "xfa/src/fxbarcode/pdf417/BC_PDF417Detector.cpp",
        "xfa/src/fxbarcode/pdf417/BC_PDF417DetectorResult.cpp",
        "xfa/src/fxbarcode/pdf417/BC_PDF417Dimensions.cpp",
        "xfa/src/fxbarcode/pdf417/BC_PDF417ECErrorCorrection.cpp",
        "xfa/src/fxbarcode/pdf417/BC_PDF417ECModulusGF.cpp",
        "xfa/src/fxbarcode/pdf417/BC_PDF417ECModulusPoly.cpp",
        "xfa/src/fxbarcode/pdf417/BC_PDF417ErrorCorrection.cpp",
        "xfa/src/fxbarcode/pdf417/BC_PDF417HighLevelEncoder.cpp",
        "xfa/src/fxbarcode/pdf417/BC_PDF417Reader.cpp",
        "xfa/src/fxbarcode/pdf417/BC_PDF417ResultMetadata.cpp",
        "xfa/src/fxbarcode/pdf417/BC_PDF417ScanningDecoder.cpp",
        "xfa/src/fxbarcode/pdf417/BC_PDF417Writer.cpp",
        "xfa/src/fxbarcode/pdf417/BC_PDF417.h",
        "xfa/src/fxbarcode/pdf417/BC_PDF417BarcodeMatrix.h",
        "xfa/src/fxbarcode/pdf417/BC_PDF417BarcodeMetadata.h",
        "xfa/src/fxbarcode/pdf417/BC_PDF417BarcodeRow.h",
        "xfa/src/fxbarcode/pdf417/BC_PDF417BarcodeValue.h",
        "xfa/src/fxbarcode/pdf417/BC_PDF417BoundingBox.h",
        "xfa/src/fxbarcode/pdf417/BC_PDF417Codeword.h",
        "xfa/src/fxbarcode/pdf417/BC_PDF417CodewordDecoder.h",
        "xfa/src/fxbarcode/pdf417/BC_PDF417Common.h",
        "xfa/src/fxbarcode/pdf417/BC_PDF417Compaction.h",
        "xfa/src/fxbarcode/pdf417/BC_PDF417DecodedBitStreamParser.h",
        "xfa/src/fxbarcode/pdf417/BC_PDF417DetectionResult.h",
        "xfa/src/fxbarcode/pdf417/BC_PDF417DetectionResultColumn.h",
        "xfa/src/fxbarcode/pdf417/BC_PDF417DetectionResultRowIndicatorColumn.h",
        "xfa/src/fxbarcode/pdf417/BC_PDF417Detector.h",
        "xfa/src/fxbarcode/pdf417/BC_PDF417DetectorResult.h",
        "xfa/src/fxbarcode/pdf417/BC_PDF417Dimensions.h",
        "xfa/src/fxbarcode/pdf417/BC_PDF417ECErrorCorrection.h",
        "xfa/src/fxbarcode/pdf417/BC_PDF417ECModulusGF.h",
        "xfa/src/fxbarcode/pdf417/BC_PDF417ECModulusPoly.h",
        "xfa/src/fxbarcode/pdf417/BC_PDF417ErrorCorrection.h",
        "xfa/src/fxbarcode/pdf417/BC_PDF417HighLevelEncoder.h",
        "xfa/src/fxbarcode/pdf417/BC_PDF417Reader.h",
        "xfa/src/fxbarcode/pdf417/BC_PDF417ResultMetadata.h",
        "xfa/src/fxbarcode/pdf417/BC_PDF417ScanningDecoder.h",
        "xfa/src/fxbarcode/pdf417/BC_PDF417Writer.h",
        "xfa/src/fxbarcode/qrcode/BC_QRAlignmentPattern.cpp",
        "xfa/src/fxbarcode/qrcode/BC_QRAlignmentPatternFinder.cpp",
        "xfa/src/fxbarcode/qrcode/BC_QRBitMatrixParser.cpp",
        "xfa/src/fxbarcode/qrcode/BC_QRCoder.cpp",
        "xfa/src/fxbarcode/qrcode/BC_QRCoderBitVector.cpp",
        "xfa/src/fxbarcode/qrcode/BC_QRCoderBlockPair.cpp",
        "xfa/src/fxbarcode/qrcode/BC_QRCoderDecoder.cpp",
        "xfa/src/fxbarcode/qrcode/BC_QRCodeReader.cpp",
        "xfa/src/fxbarcode/qrcode/BC_QRCoderECB.cpp",
        "xfa/src/fxbarcode/qrcode/BC_QRCoderECBlocks.cpp",
        "xfa/src/fxbarcode/qrcode/BC_QRCoderEncoder.cpp",
        "xfa/src/fxbarcode/qrcode/BC_QRCoderErrorCorrectionLevel.cpp",
        "xfa/src/fxbarcode/qrcode/BC_QRCoderFormatInformation.cpp",
        "xfa/src/fxbarcode/qrcode/BC_QRCoderMaskUtil.cpp",
        "xfa/src/fxbarcode/qrcode/BC_QRCoderMatrixUtil.cpp",
        "xfa/src/fxbarcode/qrcode/BC_QRCoderMode.cpp",
        "xfa/src/fxbarcode/qrcode/BC_QRCoderVersion.cpp",
        "xfa/src/fxbarcode/qrcode/BC_QRCodeWriter.cpp",
        "xfa/src/fxbarcode/qrcode/BC_QRDataBlock.cpp",
        "xfa/src/fxbarcode/qrcode/BC_QRDataMask.cpp",
        "xfa/src/fxbarcode/qrcode/BC_QRDecodedBitStreamParser.cpp",
        "xfa/src/fxbarcode/qrcode/BC_QRDetector.cpp",
        "xfa/src/fxbarcode/qrcode/BC_QRDetectorResult.cpp",
        "xfa/src/fxbarcode/qrcode/BC_QRFinderPattern.cpp",
        "xfa/src/fxbarcode/qrcode/BC_QRFinderPatternFinder.cpp",
        "xfa/src/fxbarcode/qrcode/BC_QRGridSampler.cpp",
        "xfa/src/fxbarcode/qrcode/BC_QRAlignmentPattern.h",
        "xfa/src/fxbarcode/qrcode/BC_QRAlignmentPatternFinder.h",
        "xfa/src/fxbarcode/qrcode/BC_QRBitMatrixParser.h",
        "xfa/src/fxbarcode/qrcode/BC_QRCoder.h",
        "xfa/src/fxbarcode/qrcode/BC_QRCoderBitVector.h",
        "xfa/src/fxbarcode/qrcode/BC_QRCoderBlockPair.h",
        "xfa/src/fxbarcode/qrcode/BC_QRCoderDecoder.h",
        "xfa/src/fxbarcode/qrcode/BC_QRCodeReader.h",
        "xfa/src/fxbarcode/qrcode/BC_QRCoderECB.h",
        "xfa/src/fxbarcode/qrcode/BC_QRCoderECBlocks.h",
        "xfa/src/fxbarcode/qrcode/BC_QRCoderEncoder.h",
        "xfa/src/fxbarcode/qrcode/BC_QRCoderErrorCorrectionLevel.h",
        "xfa/src/fxbarcode/qrcode/BC_QRCoderFormatInformation.h",
        "xfa/src/fxbarcode/qrcode/BC_QRCoderMaskUtil.h",
        "xfa/src/fxbarcode/qrcode/BC_QRCoderMatrixUtil.h",
        "xfa/src/fxbarcode/qrcode/BC_QRCoderMode.h",
        "xfa/src/fxbarcode/qrcode/BC_QRCoderVersion.h",
        "xfa/src/fxbarcode/qrcode/BC_QRCodeWriter.h",
        "xfa/src/fxbarcode/qrcode/BC_QRDataBlock.h",
        "xfa/src/fxbarcode/qrcode/BC_QRDataMask.h",
        "xfa/src/fxbarcode/qrcode/BC_QRDecodedBitStreamParser.h",
        "xfa/src/fxbarcode/qrcode/BC_QRDetector.h",
        "xfa/src/fxbarcode/qrcode/BC_QRDetectorResult.h",
        "xfa/src/fxbarcode/qrcode/BC_QRFinderPattern.h",
        "xfa/src/fxbarcode/qrcode/BC_QRFinderPatternFinder.h",
        "xfa/src/fxbarcode/qrcode/BC_QRGridSampler.h",
        "xfa/src/fxbarcode/qrcode/BC_FinderPatternInfo.cpp",
        "xfa/src/fxbarcode/qrcode/BC_FinderPatternInfo.h",
        "xfa/src/fxbarcode/BC_BarCode.cpp",
        "xfa/src/fxbarcode/BC_Binarizer.cpp",
        "xfa/src/fxbarcode/BC_BinaryBitmap.cpp",
        "xfa/src/fxbarcode/BC_BufferedImageLuminanceSource.cpp",
        "xfa/src/fxbarcode/BC_Dimension.cpp",
        "xfa/src/fxbarcode/BC_Library.cpp",
        "xfa/src/fxbarcode/BC_LuminanceSource.cpp",
        "xfa/src/fxbarcode/BC_Reader.cpp",
        "xfa/src/fxbarcode/BC_ResultPoint.cpp",
        "xfa/src/fxbarcode/BC_TwoDimWriter.cpp",
        "xfa/src/fxbarcode/BC_UtilCodingConvert.cpp",
        "xfa/src/fxbarcode/BC_UtilRSS.cpp",
        "xfa/src/fxbarcode/BC_Utils.cpp",
        "xfa/src/fxbarcode/BC_Writer.cpp",
        "xfa/src/fxbarcode/BC_Binarizer.h",
        "xfa/src/fxbarcode/BC_BinaryBitmap.h",
        "xfa/src/fxbarcode/BC_BufferedImageLuminanceSource.h",
        "xfa/src/fxbarcode/BC_DecoderResult.h",
        "xfa/src/fxbarcode/BC_Dimension.h",
        "xfa/src/fxbarcode/BC_LuminanceSource.h",
        "xfa/src/fxbarcode/BC_Reader.h",
        "xfa/src/fxbarcode/BC_ResultPoint.h",
        "xfa/src/fxbarcode/BC_TwoDimWriter.h",
        "xfa/src/fxbarcode/BC_UtilCodingConvert.h",
        "xfa/src/fxbarcode/BC_UtilRSS.h",
        "xfa/src/fxbarcode/BC_Writer.h",
        "xfa/src/fxbarcode/utils.h",
        "xfa/src/fxfa/src/app/xfa_checksum.cpp",
        "xfa/src/fxfa/src/app/xfa_checksum.h",
        "xfa/src/fxfa/src/app/xfa_ffapp.cpp",
        "xfa/src/fxfa/src/app/xfa_ffapp.h",
        "xfa/src/fxfa/src/app/xfa_ffbarcode.cpp",
        "xfa/src/fxfa/src/app/xfa_ffbarcode.h",
        "xfa/src/fxfa/src/app/xfa_ffcheckbutton.cpp",
        "xfa/src/fxfa/src/app/xfa_ffcheckbutton.h",
        "xfa/src/fxfa/src/app/xfa_ffchoicelist.cpp",
        "xfa/src/fxfa/src/app/xfa_ffchoicelist.h",
        "xfa/src/fxfa/src/app/xfa_ffdoc.cpp",
        "xfa/src/fxfa/src/app/xfa_ffdoc.h",
        "xfa/src/fxfa/src/app/xfa_ffdochandler.cpp",
        "xfa/src/fxfa/src/app/xfa_ffdochandler.h",
        "xfa/src/fxfa/src/app/xfa_ffdocview.cpp",
        "xfa/src/fxfa/src/app/xfa_ffdocview.h",
        "xfa/src/fxfa/src/app/xfa_ffdraw.cpp",
        "xfa/src/fxfa/src/app/xfa_ffdraw.h",
        "xfa/src/fxfa/src/app/xfa_ffexclgroup.cpp",
        "xfa/src/fxfa/src/app/xfa_ffexclgroup.h",
        "xfa/src/fxfa/src/app/xfa_fffield.cpp",
        "xfa/src/fxfa/src/app/xfa_fffield.h",
        "xfa/src/fxfa/src/app/xfa_ffimage.cpp",
        "xfa/src/fxfa/src/app/xfa_ffimage.h",
        "xfa/src/fxfa/src/app/xfa_ffimageedit.cpp",
        "xfa/src/fxfa/src/app/xfa_ffimageedit.h",
        "xfa/src/fxfa/src/app/xfa_ffnotify.cpp",
        "xfa/src/fxfa/src/app/xfa_ffnotify.h",
        "xfa/src/fxfa/src/app/xfa_ffpageview.cpp",
        "xfa/src/fxfa/src/app/xfa_ffpageview.h",
        "xfa/src/fxfa/src/app/xfa_ffpath.cpp",
        "xfa/src/fxfa/src/app/xfa_ffpath.h",
        "xfa/src/fxfa/src/app/xfa_ffpushbutton.cpp",
        "xfa/src/fxfa/src/app/xfa_ffpushbutton.h",
        "xfa/src/fxfa/src/app/xfa_ffsignature.cpp",
        "xfa/src/fxfa/src/app/xfa_ffsignature.h",
        "xfa/src/fxfa/src/app/xfa_ffsubform.cpp",
        "xfa/src/fxfa/src/app/xfa_ffsubform.h",
        "xfa/src/fxfa/src/app/xfa_fftext.cpp",
        "xfa/src/fxfa/src/app/xfa_fftext.h",
        "xfa/src/fxfa/src/app/xfa_fftextedit.cpp",
        "xfa/src/fxfa/src/app/xfa_fftextedit.h",
        "xfa/src/fxfa/src/app/xfa_ffwidget.cpp",
        "xfa/src/fxfa/src/app/xfa_ffwidget.h",
        "xfa/src/fxfa/src/app/xfa_ffwidgetacc.cpp",
        "xfa/src/fxfa/src/app/xfa_ffwidgetacc.h",
        "xfa/src/fxfa/src/app/xfa_ffwidgethandler.cpp",
        "xfa/src/fxfa/src/app/xfa_ffwidgethandler.h",
        "xfa/src/fxfa/src/app/xfa_fontmgr.cpp",
        "xfa/src/fxfa/src/app/xfa_fontmgr.h",
        "xfa/src/fxfa/src/app/xfa_fwladapter.cpp",
        "xfa/src/fxfa/src/app/xfa_fwladapter.h",
        "xfa/src/fxfa/src/app/xfa_fwltheme.cpp",
        "xfa/src/fxfa/src/app/xfa_fwltheme.h",
        "xfa/src/fxfa/src/app/xfa_rendercontext.cpp",
        "xfa/src/fxfa/src/app/xfa_rendercontext.h",
        "xfa/src/fxfa/src/app/xfa_textlayout.cpp",
        "xfa/src/fxfa/src/app/xfa_textlayout.h",
        "xfa/src/fxfa/src/common/fxfa_localevalue.h",
        "xfa/src/fxfa/src/common/xfa_docdata.h",
        "xfa/src/fxfa/src/common/xfa_doclayout.h",
        "xfa/src/fxfa/src/common/xfa_document.h",
        "xfa/src/fxfa/src/common/xfa_fm2jsapi.h",
        "xfa/src/fxfa/src/common/xfa_localemgr.h",
        "xfa/src/fxfa/src/common/xfa_object.h",
        "xfa/src/fxfa/src/common/xfa_parser.h",
        "xfa/src/fxfa/src/common/xfa_script.h",
        "xfa/src/fxfa/src/common/xfa_utils.h",
        "xfa/src/fxfa/src/fm2js/xfa_error.cpp",
        "xfa/src/fxfa/src/fm2js/xfa_error.h",
        "xfa/src/fxfa/src/fm2js/xfa_expression.cpp",
        "xfa/src/fxfa/src/fm2js/xfa_expression.h",
        "xfa/src/fxfa/src/fm2js/xfa_fm2jsapi.cpp",
        "xfa/src/fxfa/src/fm2js/xfa_fm2jscontext.cpp",
        "xfa/src/fxfa/src/fm2js/xfa_fm2jscontext.h",
        "xfa/src/fxfa/src/fm2js/xfa_fmparse.cpp",
        "xfa/src/fxfa/src/fm2js/xfa_fmparse.h",
        "xfa/src/fxfa/src/fm2js/xfa_lexer.cpp",
        "xfa/src/fxfa/src/fm2js/xfa_lexer.h",
        "xfa/src/fxfa/src/fm2js/xfa_program.cpp",
        "xfa/src/fxfa/src/fm2js/xfa_program.h",
        "xfa/src/fxfa/src/fm2js/xfa_simpleexpression.cpp",
        "xfa/src/fxfa/src/fm2js/xfa_simpleexpression.h",
        "xfa/src/fxfa/src/parser/xfa_basic_data.cpp",
        "xfa/src/fxfa/src/parser/xfa_basic_data.h",
        "xfa/src/fxfa/src/parser/xfa_basic_imp.cpp",
        "xfa/src/fxfa/src/parser/xfa_basic_imp.h",
        "xfa/src/fxfa/src/parser/xfa_document_datadescription_imp.cpp",
        "xfa/src/fxfa/src/parser/xfa_document_datadescription_imp.h",
        "xfa/src/fxfa/src/parser/xfa_document_datamerger_imp.cpp",
        "xfa/src/fxfa/src/parser/xfa_document_datamerger_imp.h",
        "xfa/src/fxfa/src/parser/xfa_document_imp.cpp",
        "xfa/src/fxfa/src/parser/xfa_document_layout_imp.cpp",
        "xfa/src/fxfa/src/parser/xfa_document_layout_imp.h",
        "xfa/src/fxfa/src/parser/xfa_document_serialize.cpp",
        "xfa/src/fxfa/src/parser/xfa_document_serialize.h",
        "xfa/src/fxfa/src/parser/xfa_layout_appadapter.cpp",
        "xfa/src/fxfa/src/parser/xfa_layout_appadapter.h",
        "xfa/src/fxfa/src/parser/xfa_layout_itemlayout.cpp",
        "xfa/src/fxfa/src/parser/xfa_layout_itemlayout.h",
        "xfa/src/fxfa/src/parser/xfa_layout_pagemgr_new.cpp",
        "xfa/src/fxfa/src/parser/xfa_layout_pagemgr_new.h",
        "xfa/src/fxfa/src/parser/xfa_locale.cpp",
        "xfa/src/fxfa/src/parser/xfa_locale.h",
        "xfa/src/fxfa/src/parser/xfa_localemgr.cpp",
        "xfa/src/fxfa/src/parser/xfa_localevalue.cpp",
        "xfa/src/fxfa/src/parser/xfa_objectacc_imp.cpp",
        "xfa/src/fxfa/src/parser/xfa_object_imp.cpp",
        "xfa/src/fxfa/src/parser/xfa_parser_imp.cpp",
        "xfa/src/fxfa/src/parser/xfa_parser_imp.h",
        "xfa/src/fxfa/src/parser/xfa_script_datawindow.cpp",
        "xfa/src/fxfa/src/parser/xfa_script_datawindow.h",
        "xfa/src/fxfa/src/parser/xfa_script_eventpseudomodel.cpp",
        "xfa/src/fxfa/src/parser/xfa_script_eventpseudomodel.h",
        "xfa/src/fxfa/src/parser/xfa_script_hostpseudomodel.cpp",
        "xfa/src/fxfa/src/parser/xfa_script_hostpseudomodel.h",
        "xfa/src/fxfa/src/parser/xfa_script_imp.cpp",
        "xfa/src/fxfa/src/parser/xfa_script_imp.h",
        "xfa/src/fxfa/src/parser/xfa_script_layoutpseudomodel.cpp",
        "xfa/src/fxfa/src/parser/xfa_script_layoutpseudomodel.h",
        "xfa/src/fxfa/src/parser/xfa_script_logpseudomodel.cpp",
        "xfa/src/fxfa/src/parser/xfa_script_logpseudomodel.h",
        "xfa/src/fxfa/src/parser/xfa_script_nodehelper.cpp",
        "xfa/src/fxfa/src/parser/xfa_script_nodehelper.h",
        "xfa/src/fxfa/src/parser/xfa_script_resolveprocessor.cpp",
        "xfa/src/fxfa/src/parser/xfa_script_resolveprocessor.h",
        "xfa/src/fxfa/src/parser/xfa_script_signaturepseudomodel.cpp",
        "xfa/src/fxfa/src/parser/xfa_script_signaturepseudomodel.h",
        "xfa/src/fxfa/src/parser/xfa_utils_imp.cpp",
        "xfa/src/fxgraphics/src/fx_graphics.cpp",
        "xfa/src/fxgraphics/src/fx_path_generator.cpp",
        "xfa/src/fxgraphics/src/fx_path_generator.h",
        "xfa/src/fxgraphics/src/pre.h",
      ],
      "conditions": [
        ["clang==1" , {
          # TODO(tsepez): remove this when FX fixes warnings
          "cflags": [
            "-Wno-deprecated-declarations"
          ],
        }],
        ["pdf_enable_v8==1", {
          'dependencies': [
            '<(DEPTH)/v8/tools/gyp/v8.gyp:v8',
          ],
          'export_dependent_settings': [
            '<(DEPTH)/v8/tools/gyp/v8.gyp:v8',
          ],
          'include_dirs': [
            '<(DEPTH)/v8',
            '<(DEPTH)/v8/include',
          ],
          'sources': [
            "xfa/src/fxjse/src/class.cpp",
            "xfa/src/fxjse/src/class.h",
            "xfa/src/fxjse/src/context.cpp",
            "xfa/src/fxjse/src/context.h",
            "xfa/src/fxjse/src/dynprop.cpp",
            "xfa/src/fxjse/src/runtime.cpp",
            "xfa/src/fxjse/src/runtime.h",
            "xfa/src/fxjse/src/scope_inline.h",
            "xfa/src/fxjse/src/util_inline.h",
            "xfa/src/fxjse/src/value.cpp",
            "xfa/src/fxjse/src/value.h"
          ],
        }],
        ["OS == 'win'", {
          "configurations": {
            "Debug": {
              "msvs_configuration_attributes": {},
              "msvs_settings": {
                "VCCLCompilerTool": {},
                "VCLibrarianTool": {},
                "VCLinkerTool": {},
              }
            },
            "Release": {
              "msvs_configuration_attributes": {},
              "msvs_settings": {
                "VCCLCompilerTool": {},
                "VCLibrarianTool": {},
                "VCLinkerTool": {},
              }
            }
            },
          "sources": [],
        }],
        ["OS == 'mac'", {
          "configurations": {},
          "sources": [],
          "cflags": [ "-Wno-deprecated-declarations" ],
          "defines!": [ "V8_DEPRECATION_WARNINGS" ],
        }],
      ]
    }
  ]
}
