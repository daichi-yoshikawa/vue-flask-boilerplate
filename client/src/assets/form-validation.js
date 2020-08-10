function isEmpty(text) {
  return !text.trim();
}

export function validateLength(text, options={}) {
  minLength = typeof options.minLength !== 'undefined' ? options.minLength : 4;
  maxLength = typeof options.maxLength !== 'undefined' ? options.maxLength : 64;

  if(isEmpty(text)) {
    return false;
  }

  if(typeof options.minLength !== 'undefined') {
    if(options.minLength > trim_text.length) {
      return false;
    }
  }

  if(typeof options.maxLength !== 'undefined') {
    if(options.maxLength < trim_text.length) {
      return false;
    }
  }

  return true;
}

export function validateEmail(text) {
  const REGEX_EMAIL = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return REGEX_EMAIL.test(text)
}

