let copyList  = document.querySelectorAll( '.copy-clipboard' );
let copyArray = Array.prototype.slice.call( copyList );

function tooltipUpdate( button, tooltip, title ) {
  tooltip.dispose();
  button.setAttribute( 'title', title );
  tooltip = new bootstrap.Tooltip( button );
  tooltip.show();

  return tooltip;
}

copyArray.map( function ( copy ) {
  let text    = copy.querySelector( 'span' ).innerText;
  let button  = copy.querySelector( 'i' );
  let tooltip = new bootstrap.Tooltip( button );

  button.addEventListener( 'mouseover', function () {
    tooltip = tooltipUpdate( button, tooltip, 'Скопировать' );
    this.classList.remove( 'bi-clipboard-check' );
    this.classList.add( 'bi-clipboard-plus' );
  } );

  button.addEventListener( 'click', function () {
    window.navigator.clipboard.writeText( text );
    tooltip = tooltipUpdate( button, tooltip, 'Готово!' );
    this.classList.remove( 'bi-clipboard-plus' );
    this.classList.add( 'bi-clipboard-check' );
  } );
} );