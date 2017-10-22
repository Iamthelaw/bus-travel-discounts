// This is where csrf token passed to every request
$(document).on('ajaxBeforeSend', function(e, xhr, options) {
  xhr.setRequestHeader("X-CSRFToken", $('[name=csrfmiddlewaretoken]').val());
});

console.log($('[name=csrfmiddlewaretoken]').val())
console.log('hi')

var App = (function() {
    return {
        init: function() {
            this.cacheElements();
            this.hideElements();
            this.bindEvents();
            this.user,
            this.url = {
                register: '/auth/register/',
            };
        },
        cacheElements: function() {
            this.modal = {
                $window: $('#js-modal-window'),
                $closeBtn: $('#js-modal-close-btn'),
                $title: $('#js-modal-title'),
                $loginForm: $('#js-login-form'),
                $registerForm: $('#js-register-form'),
                $registerBtn: $('#js-register-btn'),
                activeClass: 'active',
            };
            this.leader = {
                $registerForm: $('#js-leader-register-form'),
                $infoBlock: $('#js-leader-info-block'),
            }
            this.$loginBtn = $('#js-login-btn');
        },
        hideElements: function() {
            this.leader.$infoBlock.hide();
        },
        bindEvents: function() {
            this.$loginBtn.on('click', this.showLoginModal.bind(this));
            this.modal.$closeBtn.on('click', this.closeModal.bind(this));
            this.modal.$registerBtn.on('click', this.showRegisterModal.bind(this));
            this.leader.$registerForm.on('submit', this.sendRegisterRequest.bind(this));
            $(document).keyup(this.closeModalOnEsc.bind(this));
        },
        closeModal: function(e) {
            e.preventDefault();
            this.modal.$window.removeClass(this.modal.activeClass);
        },
        closeModalOnEsc: function(e) {
            if (e.keyCode == 27) {
                this.modal.$window.removeClass(this.modal.activeClass);
            }
        },
        showModal: function() {
            this.modal.$window.addClass(this.modal.activeClass);
        },
        sendRegisterRequest: function(e) {
            e.preventDefault();
            var that = this,
                block = that.leader.$infoBlock;
            block.hide();
            $.post(that.url.register, that.leader.$registerForm.serialize())
                .done(
                    function(data) {
                        that.user = data.username;
                        block.addClass('toast-success');
                        block.text('Your user created successfully!');
                        block.show();
                        that.leader.$registerForm.hide();
                    })
                .fail(
                    function(xhr){
                        if(xhr.readyState == 4 && xhr.status == 400) {
                            var res = JSON.parse(xhr.response);
                            block.addClass('toast-error');
                            block.text(Object.values(res))
                            block.show();
                        }
                });
        },
        setModalTitle: function(title) {
            this.modal.$title.text(title);
        },
        showLoginModal: function(e) {
            e.preventDefault();
            this.showModal();
            this.setModalTitle('Login');
            this.modal.$loginForm.show();
            this.modal.$registerForm.hide();
        },
        showRegisterModal: function(e) {
            e.preventDefault();
            this.setModalTitle('Register');
            this.modal.$loginForm.hide();
            this.modal.$registerForm.show();
        }
    }
})()
App.init();