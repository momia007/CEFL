// static/js/val_cuil.js

function validarCUIL(cuil) {
  if (!/^\d{11}$/.test(cuil)) return false;

  const coef = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2];
  let suma = 0;

  for (let i = 0; i < 10; i++) {
    suma += parseInt(cuil[i]) * coef[i];
  }

  const verificador = 11 - (suma % 11);
  const digito = verificador === 11 ? 0 : verificador === 10 ? 9 : verificador;

  return digito === parseInt(cuil[10]);
}
