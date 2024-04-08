CKEDITOR.replace('description-container', {
    // Define toolbar groups as arrays of buttons
    toolbar: [
        { name: 'document', groups: ['mode', 'document', 'doctools'], items: ['Source'] },
        { name: 'clipboard', groups: ['clipboard', 'undo'], items: ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo'] },
        { name: 'styles', items: ['Format', 'Styles'] },
        { name: 'basicstyles', groups: ['basicstyles', 'cleanup'], items: ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat'] },
        { name: 'paragraph', groups: ['list', 'indent', 'blocks', 'align', 'bidi'], items: ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'] },
        { name: 'links', items: ['Link', 'Unlink', 'Anchor'] },
        { name: 'insert', items: ['Image', 'Table', 'HorizontalRule', 'SpecialChar'] },
        '/',
        { name: 'colors', items: ['TextColor', 'BGColor'] },
        { name: 'tools', items: ['Maximize'] }
    ],

    // Define styles for the Format dropdown
    stylesSet: [
        { name: 'Normal', element: 'p' },
        { name: 'Heading 1', element: 'h1' },
        { name: 'Heading 2', element: 'h2' },
        { name: 'Heading 3', element: 'h3' },
        { name: 'Heading 4', element: 'h4' },
        { name: 'Heading 5', element: 'h5' },
        { name: 'Heading 6', element: 'h6' }
    ],

    // Allow tables to be inserted
    extraAllowedContent: 'table;td;th;caption;tbody;tr;thead',

    // Enable content filtering to prevent unwanted HTML tags and attributes
    extraAllowedContent: '*(*)[*];div(*)',
    disallowedContent: 'script;iframe;object;embed',
});
